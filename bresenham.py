import matplotlib.pyplot as plt

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

err = dx - dy

X, Y = [], []

while True:
    X.append(x1)
    Y.append(y1)

    if x1 == x2 and y1 == y2:
        break

    e = 2 * err

    if e > -dy:
        err -= dy
        x1 += sx

    if e < dx:
        err += dx
        y1 += sy

plt.scatter(X, Y)
plt.plot(X, Y, linewidth=0.5)
plt.grid()
plt.axis("equal")
plt.show()