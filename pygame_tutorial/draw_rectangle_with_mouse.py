import pygame
from pygame.locals import*

red=(255,0,0)
blue=(0,255,0)
green=(0,0,255)
black=(0,0,0)
white=(255,255,255)
screen=pygame.display.set_mode((600,400))
screen.fill(green)
pygame.display.update()
start=(0,0)
size=(0,0)
drawing=False
run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        elif i.type==MOUSEBUTTONUP:
            end=i.pos
            size=end[0]-start[0],end[1]-start[1]
            drawing=False
        elif i.type==MOUSEBUTTONDOWN:
            start=i.pos
            size=0,0
            drawing=True
        elif i.type==MOUSEMOTION and drawing:
            end=i.pos
            size=end[0]-start[0],end[1]-start[1]
        pygame.draw.rect(screen,blue,(start,size),2)
        pygame.display.update()
pygame.quit()
