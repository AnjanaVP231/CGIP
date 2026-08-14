import pygame
pygame.init()
screen = pygame.display.set_mode((600, 500))

xc, yc = map(int, input("Enter center xc yc: ").split())
r = int(input("Enter radius: "))
x, y = 0, r
p = 1 - r

while x <= y:
    for a, b in [(x,y), (-x,y), (x,-y), (-x,-y),
                 (y,x), (-y,x), (y,-x), (-y,-x)]:
        screen.set_at((xc+a, yc+b), (255, 255, 255))
    x += 1
    if p < 0:
        p += 2*x + 1
    else:
        y -= 1
        p += 2*(x-y) + 1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            