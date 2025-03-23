import pygame
import random
import sys
import time
import os

pygame.init()

WIDTH, HEIGHT = 400, 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def load_image(filename):
    return pygame.image.load(os.path.join(BASE_PATH, filename))

def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(BASE_PATH, filename))

background = load_image("AnimatedStreet.png")
player_car = load_image("Player.png")
enemy_car = load_image("Enemy.png")
coin_image = load_image("Coin.png")

player_car = pygame.transform.scale(player_car, (50, 90))
enemy_car = pygame.transform.scale(enemy_car, (50, 90))
coin_image = pygame.transform.scale(coin_image, (30, 30))

pygame.mixer.music.load(os.path.join(BASE_PATH, "background.wav"))
pygame.mixer.music.play(-1)
crash_sound = load_sound("crash.wav")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_car
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_car
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-200, -50))
    
    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.rect.top = random.randint(-200, -50)
            self.rect.center = (random.randint(40, WIDTH - 40), self.rect.top)
        
        if self.rect.colliderect(P1.rect):
            COIN_SCORE += 1
            self.rect.top = random.randint(-200, -50)
            self.rect.center = (random.randint(40, WIDTH - 40), self.rect.top)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    screen.blit(background, (0, 0))
    scores = font.render(f"Score: {SCORE}", True, BLACK)
    coin_scores = font.render(f"Coins: {COIN_SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (10, 40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        screen.fill((255, 0, 0))
        game_over = font.render("Game Over", True, BLACK)
        screen.blit(game_over, (WIDTH//2 - 50, HEIGHT//2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    pygame.time.Clock().tick(60)
