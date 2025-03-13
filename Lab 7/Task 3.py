import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
BALL_SPEED = 20

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

running = True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
        ball_x -= BALL_SPEED
    if keys[pygame.K_RIGHT] and ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
        ball_x += BALL_SPEED
    if keys[pygame.K_UP] and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
        ball_y -= BALL_SPEED
    if keys[pygame.K_DOWN] and ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
        ball_y += BALL_SPEED
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.update()
    
pygame.quit()
