import pygame
import random
import psycopg2
import json
import time

pygame.init()

# Параметры окна и игры
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
SPEED = 10

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

# Параметры подключения к базе данных
conn_params = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "112430dar",
    "host": "localhost",
    "port": "5432"
}

# Подключение к базе данных
def connect():
    try:
        conn = psycopg2.connect(**conn_params)
        print("Подключение к базе данных успешно")
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None

# Проверка существования пользователя или регистрация
def get_or_register_user(username):
    conn = connect()
    if conn is None:
        print("Не удалось подключиться к базе данных")
        return None
    try:
        cur = conn.cursor()
        print(f"Проверка пользователя: {username}")
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            print(f"Пользователь {username} найден, ID: {result[0]}")
            return result[0]
        print(f"Пользователь {username} не найден, регистрируем...")
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"Пользователь {username} зарегистрирован, ID: {user_id}")
        return user_id
    except Exception as e:
        print(f"Ошибка регистрации: {e}")
        return None
    finally:
        cur.close()
        conn.close()

# Сохранение состояния игры
def save_game(user_id, level, score, snake, snake_direction, food):
    conn = connect()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        state = {
            "snake": snake,
            "snake_direction": snake_direction,
            "food_x": food.x,
            "food_y": food.y,
            "food_value": food.value,
            "food_timer": food.timer
        }
        state_json = json.dumps(state)
        cur.execute(
            "INSERT INTO user_score (user_id, level, score, saved_state) VALUES (%s, %s, %s, %s)",
            (user_id, level, score, state_json)
        )
        conn.commit()
        print("Игра сохранена")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
    finally:
        cur.close()
        conn.close()

# Загрузка последнего сохраненного состояния
def load_game(user_id):
    conn = connect()
    if conn is None:
        return None
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT level, score, saved_state FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1",
            (user_id,)
        )
        result = cur.fetchone()
        if result:
            level, score, state_json = result
            state = json.loads(state_json)
            return level, score, state
        return None
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None
    finally:
        cur.close()
        conn.close()

# Класс еды
class Food:
    def __init__(self, snake, x=None, y=None, value=None, timer=None):
        if x is None or y is None:
            self.respawn(snake)
        else:
            self.x = x
            self.y = y
            self.value = value if value is not None else random.choice([1, 2, 3])
            self.timer = timer if timer is not None else 150

    def respawn(self, snake):
        while True:
            self.x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            self.y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (self.x, self.y) not in snake:
                break
        self.value = random.choice([1, 2, 3])
        self.timer = 150

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def tick(self):
        self.timer -= 1
        return self.timer <= 0

# Регистрация пользователя
username = input("Введите имя пользователя: ")
user_id = get_or_register_user(username)
if user_id is None:
    print("Не удалось зарегистрировать или найти пользователя. Выход.")
    pygame.quit()
    exit()

# Загрузка сохраненного состояния
saved_state = load_game(user_id)

# Проверка корректности сохраненного состояния
if saved_state:
    level, score, state = saved_state
    snake = state["snake"]
    snake_direction = tuple(state["snake_direction"])
    food = Food(snake, state["food_x"], state["food_y"], state["food_value"], state["food_timer"])
    # Проверяем, не приводит ли состояние к немедленному проигрышу
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    if (new_head[0] < 0 or new_head[0] >= WIDTH or 
        new_head[1] < 0 or new_head[1] >= HEIGHT or 
        new_head in snake):
        print("Сохраненное состояние некорректно, сбрасываем игру")
        snake = [(100, 100)]
        snake_direction = (CELL_SIZE, 0)
        food = Food(snake)
        score = 0
        level = 1
else:
    snake = [(100, 100)]
    snake_direction = (CELL_SIZE, 0)
    food = Food(snake)
    score = 0
    level = 1

running = True
game_over = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(user_id, level, score, snake, snake_direction, food)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Пауза на P
                paused = True
                save_game(user_id, level, score, snake, snake_direction, food)
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_p:
                            paused = False
                            break
            if not game_over:
                if event.key == pygame.K_UP and snake_direction != (0, CELL_SIZE):
                    snake_direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake_direction != (0, CELL_SIZE):
                    snake_direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake_direction != (CELL_SIZE, 0):
                    snake_direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-CELL_SIZE, 0):
                    snake_direction = (CELL_SIZE, 0)

    if not game_over:
        # Движение змейки
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        # Проверка на стены
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            save_game(user_id, level, score, snake, snake_direction, food)
            game_over = True

        # Проверка на столкновение с собой
        if new_head in snake:
            save_game(user_id, level, score, snake, snake_direction, food)
            game_over = True

        if not game_over:
            snake.insert(0, new_head)

            # Проверка на еду
            if new_head == (food.x, food.y):
                score += food.value
                if score % 4 == 0:
                    level += 1
                    SPEED += 2
                food.respawn(snake)
            else:
                snake.pop()

            if food.tick():
                food.respawn(snake)

        # Отрисовка змейки
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Отрисовка еды
        food.draw()

    # Текст
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    if game_over:
        game_over_text = font.render("Game Over! Press Q to quit", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
time.sleep(2)  # Задержка перед закрытием