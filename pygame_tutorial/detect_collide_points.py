from rect import *
pygame.display.set_caption("Collide Points")
points = random_points(100)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                points = random_points(100)
    screen.fill(gray)
    pygame.draw.rect(screen, green, rect, 8)
    for p in points:
        if rect.collidepoint(p):
            pygame.draw.circle(screen, red, p, 8, 0)
        else:
            pygame.draw.circle(screen, blue, p,8, 0)
    pygame.display.flip()
pygame.quit()
