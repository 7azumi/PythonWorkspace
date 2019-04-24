import pygame
import time


filepath = r"E:\Music\ape\The Coral Sea - In This Moment's Time.mp3"      #E:\workspace\Python\Basic\musicplayer\ztj.mp3

pygame.mixer.init()

track = pygame.mixer.music.load(filepath)

pygame.mixer.music.play()

time.sleep(10)

pygame.mixer.music.stop()