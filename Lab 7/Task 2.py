import pygame
import os

pygame.init()
pygame.mixer.init() #Аудиосистема

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Music Player")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_FOLDER = os.path.join(BASE_DIR, "music")
playlist = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith(".mp3")]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[current_track]}")

if playlist:
    play_music()
else:
    print("Нет доступных треков в папке music")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
                print("Music Resumed")
            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
                print("Music Paused")
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_b:  # Back
                current_track = (current_track - 1) % len(playlist)
                play_music()

pygame.quit()
