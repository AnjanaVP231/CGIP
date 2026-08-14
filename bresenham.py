import pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

dx, dy = abs(x2-x1), abs(y2-y1)
sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1
p = 2*dy - dx

while x1 <= x2:
    screen.set_at((x1, y1), (255, 255, 255))

    if p < 0:
        p += 2*dy
    else:
        y1 += sy
        p += 2*(dy-dx)

    x1 += sx
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            