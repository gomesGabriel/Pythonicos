import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
'''
from pygame import *
ixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
while mixer.music.get_busy():
        time.Clock().tick(10)

import playsound
playsound.playsound('ex021.mp3', True)
'''
