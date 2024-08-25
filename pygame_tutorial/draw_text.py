"""Draw text to the screen."""
import pygame
from pygame.locals import *
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Draw Text")
sysfont = pygame.font.get_default_font()
#font = pygame.font.SysFont(None, 48)
#img = font.render(sysfont, True, RED)
font1 = pygame.font.SysFont(None, 72)
img1 = font1.render('Hello....', True, BLUE)
font2 = pygame.font.SysFont(' ', 72)
img2 = font2.render('Its Yogendra ', True, GREEN)
#fonts = pygame.font.get_fonts()
#print(fonts)
running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill(background)
    #screen.blit(img,(20,20))
    screen.blit(img1, (20, 100))
    screen.blit(img2, (20, 120))
    pygame.display.update()
pygame.quit()
