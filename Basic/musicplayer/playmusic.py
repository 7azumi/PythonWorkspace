import pygame
import time


filepath = r"E:\workspace\Python\musicplayer\ztj.mp3"

pygame.mixer.init()

track = pygame.mixer.music.load(filepath)

pygame.mixer.music.play()

time.sleep(10)

pygame.mixer.music.stop()