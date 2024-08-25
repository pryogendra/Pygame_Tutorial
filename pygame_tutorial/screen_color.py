import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,400))
#col=(0,255,255)
#screen.fill(col)
screen.fill((0,255,255))
pygame.display.update()
background=(255,255,255)
run=True
for event in pygame.event.get():
    if event.type==pygame.QUIT:
        run= False
    elif event.type==pygame.KEYDOWN:
        if event.key==K_g:
            background=(0,255,0)
        elif event.key==K_r:
            background=(255,0,0)
screen.fill(background)
pygame.display.update()
pygame.quit()
