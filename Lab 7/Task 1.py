import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)

mickey_img = pygame.image.load("mickey_clock.png")
mickey_img = pygame.transform.scale(mickey_img, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

def draw_hand(angle, length, color, thickness):
    end_x = CENTER[0] + length * math.cos(math.radians(angle))
    end_y = CENTER[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), thickness)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(mickey_img, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    second_angle = 90 - (seconds * 6)
    minute_angle = 90 - (minutes * 6)
    
    draw_hand(second_angle, 100, (255, 0, 0), 3)
    draw_hand(minute_angle, 80, (0, 0, 255), 5)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
