import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Move Image")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
img=pygame.image.load("ball.jpeg")
img.convert()
rect=img.get_rect()
rect.center=800//2,500//2  #puting image at the center
run=True
moving=False
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
        if event.type==MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving=True
        elif event.type==MOUSEBUTTONUP:
            moving=False
        elif event.type==MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    screen.fill(green)
    screen.blit(img,rect)
    pygame.draw.rect(screen,red,rect,2)
    pygame.display.update()
pygame.quit()