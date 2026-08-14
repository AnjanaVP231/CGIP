import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())
dx, dy = x2 - x1, y2 - y1
steps = max(abs(dx), abs(dy))
xinc, yinc = dx / steps, dy / steps
x, y = x1, y1
for i in range(steps + 1):
    screen.set_at((round(x), round(y)), (255, 255, 255))
    x += xinc
    y += yinc
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()