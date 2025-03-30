import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500     # окно
CELL_SIZE = 20               # размер клетки для обьектов
SPEED = 10                   # начальная скорость

# цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

# еда с весом и таймером
class Food:
    def __init__(self, snake):
        self.respawn(snake)
    
    def respawn(self, snake):
        while True:
            self.x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            self.y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (self.x, self.y) not in snake:
                break
        self.value = random.choice([1, 2, 3])     # сколько даст очков
        self.timer = 150                          # сколько живет на поле в кадрах

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    def tick(self):
        self.timer -= 1
        return self.timer <= 0   # если таймер кончился, возвращает True

snake = [(100, 100)]                   # начальная змейка — одно звено
snake_direction = (CELL_SIZE, 0)      # идёт вправо
food = Food(snake)
score = 0
level = 1
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # направление — проверка чтобы не шла в себя
            if event.key == pygame.K_UP and snake_direction != (0, CELL_SIZE):
                snake_direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -CELL_SIZE):
                snake_direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (CELL_SIZE, 0):
                snake_direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-CELL_SIZE, 0):
                snake_direction = (CELL_SIZE, 0)

    # двигаем голову
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # проверка на стены
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False

    # проверка — в себя врезался
    if new_head in snake:
        running = False

    snake.insert(0, new_head)  # двигаем голову вперёд

    if new_head == (food.x, food.y):
        score += food.value
        if score % 4 == 0:
            level += 1
            SPEED += 2   #становится сложнее
        food.respawn(snake)  # новая еда
    else:
        snake.pop()  # если не съел убираем хвост (либо змея растёт)

    if food.tick():    # если еда истекает срок
        food.respawn(snake)

    # рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # рисуем еду
    food.draw()

    # текст
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
