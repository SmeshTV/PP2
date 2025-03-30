import pygame
import random
import sys
import time
import os

pygame.init()

# размеры окна
WIDTH, HEIGHT = 400, 600

# скорость падения
SPEED = 5

# очки за врагов которые едят мимо
SCORE = 0

# очки за монеты
COIN_SCORE = 0

# чтоб каждый раз не бустилась скорость на 5, а один раз
coins_checkpoint = 0

# цвет текста
BLACK = (0, 0, 0)

# окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# путь до папки, где лежит игра
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# функции загрузки изображений и звуков
def load_image(filename):
    return pygame.image.load(os.path.join(BASE_PATH, filename))

def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(BASE_PATH, filename))

# загружаем картинку дороги и машинок
background = load_image("AnimatedStreet.png")
player_car = load_image("Player.png")
enemy_car = load_image("Enemy.png")
coin_image = load_image("Coin.png")

# меняем размеры, чтобы не были огромные
player_car = pygame.transform.scale(player_car, (50, 90))
enemy_car = pygame.transform.scale(enemy_car, (50, 90))
coin_image = pygame.transform.scale(coin_image, (30, 30))

# фоновая музыка
pygame.mixer.music.load(os.path.join(BASE_PATH, "background.wav"))
pygame.mixer.music.play(-1)  # -1 значит зациклить типо повторять постоянно

# звук аварии
crash_sound = load_sound("crash.wav")

# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_car
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)  # появление внизу

    # обработка нажатий
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)  # влево
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)   # вправо

# враг, едет сверху вниз
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_car
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)  # вниз по прямой
        if self.rect.top > HEIGHT:
            SCORE += 1  # типа его объехал
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

        global coins_checkpoint
        if COIN_SCORE // 5 > coins_checkpoint:
            SPEED += 1  # каждый 5 монет буст скорости
            coins_checkpoint += 1

# монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.reset_position()

    # делаем ей новое место и новую "цену"
    def reset_position(self):
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-200, -50))
        self.value = random.choice([1, 3, 5])  # рандом очки, как повезёт

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.reset_position()
        if self.rect.colliderect(P1.rect):
            COIN_SCORE += self.value
            self.reset_position()

# создаем всех персонажей
P1 = Player()
E1 = Enemy()
C1 = Coin()

# группы объектов для управления
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# шрифт текста
font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    # рисуем фон
    screen.blit(background, (0, 0))

    # показываем очки и монеты
    scores = font.render(f"Score: {SCORE}", True, BLACK)
    coin_scores = font.render(f"Coins: {COIN_SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (10, 40))

    # обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # двигаем всех
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # если врезался во врага
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        screen.fill((255, 0, 0))
        game_over = font.render("Game Over", True, BLACK)
        screen.blit(game_over, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(60)  # 60 FPS, плавненько
