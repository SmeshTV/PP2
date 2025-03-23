import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
SPEED = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

snake = [(100, 100)]
snake_direction = (CELL_SIZE, 0)
food = generate_food(snake)
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
            if event.key == pygame.K_UP and snake_direction != (0, CELL_SIZE):
                snake_direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -CELL_SIZE):
                snake_direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (CELL_SIZE, 0):
                snake_direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-CELL_SIZE, 0):
                snake_direction = (CELL_SIZE, 0)
    
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        food = generate_food(snake)

        if score % 4 == 0:
            level += 1
            SPEED += 2 
    else:
        snake.pop()
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
