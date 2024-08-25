import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 500))
while True:
    for event in pygame.event.get():
        print(event)
pygame.quit()
