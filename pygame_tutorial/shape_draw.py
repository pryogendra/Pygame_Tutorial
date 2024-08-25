import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500)) #set pygame display
red=(255,0,0)
green=(0,0,255)
white=(255,255,255)
screen.fill(red)  #fill screen with red color
pygame.display.update()
running=True
pygame.draw.rect(screen,green,(100,10,100,100)) #rectangle
pygame.draw.rect(screen,white,(150,60,100,100),9)  #rectangle
pygame.draw.ellipse(screen,green,(250,10,100,100))  #ellipse
pygame.draw.ellipse(screen,white,(300,60,100,100),9)  #ellipse
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
