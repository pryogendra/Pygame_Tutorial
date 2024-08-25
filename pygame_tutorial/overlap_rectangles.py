from rect import *
n = 30
pygame.display.set_caption("Overlap Rectangles")
rects = random_rects(n)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                rects = random_rects(n)
    screen.fill(gray)
    intersecting = []
    for i in range(n-1):
        r0 = rects[i]
        for j in range(i+1, n):
            r1 = rects[j]
            if r0.colliderect(r1):
                intersecting.append(r0)
                intersecting.append(r1)
                break
    for i, r in enumerate(rects):
        color = red if r in intersecting else blue
        pygame.draw.rect(screen, color, r)
        draw_text(str(i), r.topleft)
    pygame.display.flip()
pygame.quit()