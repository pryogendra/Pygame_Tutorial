from rect import *
n = 50
pygame.display.set_caption("Collide Rectangle")
rects = random_rects(n)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                rects = random_rects(n)
    screen.fill(gray)
    pygame.draw.rect(screen, green, rect, 4)
    for r in rects:
        if rect.colliderect(r):
            pygame.draw.rect(screen, red, r, 4)
        else:
            pygame.draw.rect(screen, blue, r, 4)
    pygame.display.flip()
pygame.quit()