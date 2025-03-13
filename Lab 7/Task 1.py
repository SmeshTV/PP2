import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 750, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)

mickey_img = pygame.image.load("mickey_clock.jpg")
mickey_img = pygame.transform.scale(mickey_img, (WIDTH, HEIGHT))
min_hand_img = pygame.image.load("min_hand.png")
sec_hand_img = pygame.image.load("sec_hand.png")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

def draw_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=CENTER)
    screen.blit(rotated_image, rect.topleft)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(mickey_img, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    second_angle = -(seconds * 6)
    minute_angle = -(minutes * 6)
    
    draw_hand(sec_hand_img, second_angle)
    draw_hand(min_hand_img, minute_angle)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()