import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

drawing = False
last_pos = None
color = BLACK
brush_size = 5
mode = "brush"

screen.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_b:
                mode = "brush"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, color, last_pos, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size)
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "rect":
                rect_start = event.pos
            elif mode == "circle":
                circle_start = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rect":
                rect_end = event.pos
                pygame.draw.rect(screen, color, (*rect_start, rect_end[0] - rect_start[0], rect_end[1] - rect_start[1]), 2)
            elif mode == "circle":
                circle_end = event.pos
                radius = int(((circle_end[0] - circle_start[0])**2 + (circle_end[1] - circle_start[1])**2)**0.5)
                pygame.draw.circle(screen, color, circle_start, radius, 2)

    pygame.display.flip()

pygame.quit()
