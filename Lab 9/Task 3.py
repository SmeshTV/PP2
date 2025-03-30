import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

# цвета используем для кисти и фигур
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

# переменные
drawing = False         # рисуем ли в данный момент
last_pos = None         # последняя позиция мышки
color = BLACK           # начальный цвет чёрный
brush_size = 5          # толщина кисти
mode = "brush"          # текущий режим рисования

start_pos = None        # где нажал мышкой
end_pos = None          # где отпустил мышку

# фон белый
screen.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # проверка на нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            # фигуры
            if event.key == pygame.K_r:
                mode = "rect"         # прямоугольник
            elif event.key == pygame.K_c:
                mode = "circle"       # круг
            elif event.key == pygame.K_b:
                mode = "brush"        # кисть
            elif event.key == pygame.K_e:
                mode = "eraser"       # ластик
            elif event.key == pygame.K_s:
                mode = "square"       # квадрат
            elif event.key == pygame.K_t:
                mode = "triangle"     # прямоугольный треугольник
            elif event.key == pygame.K_q:
                mode = "equal_triangle" # равносторонний треугольник
            elif event.key == pygame.K_h:
                mode = "rhombus"      # ромб

            # цвета
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        # нажал мышкой
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        # отпустил мышку
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            # прямоугольник
            if mode == "rect":
                pygame.draw.rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)

            # квадрат- берём минимальную сторону, чтобы был ровный
            elif mode == "square":
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, color, (x1, y1, side, side), 2)

            # прямоугольный треугольник правый угол внизу
            elif mode == "triangle":
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            # равносторонний треугольник
            elif mode == "equal_triangle":
                height = abs(y2 - y1)
                half_base = height / math.tan(math.radians(60))
                points = [
                    (x1, y2),
                    (x1 + half_base, y1),
                    (x1 + 2 * half_base, y2)
                ]
                pygame.draw.polygon(screen, color, points, 2)

            # ромб- середина между точками, и рисуем 4 угла
            elif mode == "rhombus":
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, y1),    # верх
                    (x2, center_y),    # правый
                    (center_x, y2),    # низ
                    (x1, center_y)     # левый
                ]
                pygame.draw.polygon(screen, color, points, 2)

            # круг- считаем расстояние как радиус
            elif mode == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        # движение мышки + нажата кнопка
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, color, last_pos, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size)
            last_pos = event.pos

    pygame.display.flip()

pygame.quit()

# b - кисть
# e - ластик
# r - прямоугольник
# s - квадрат
# t - прямоугольный треугольник
# q - равносторонний треугольник
# h - ромб
# c - круг

# 1 - чёрный цвет
# 2 - красный цвет
# 3 - зелёный цвет
# 4 - синий цвет
