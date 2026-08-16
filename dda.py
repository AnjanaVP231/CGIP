import matplotlib.pyplot as plt
x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())
dx, dy = x2-x1, y2-y1

steps = max(abs(dx), abs(dy))
xinc = dx / steps
yinc = dy / steps
x, y = x1, y1

X, Y = [], []
for i in range(steps + 1):
    X.append(round(x))
    Y.append(round(y))
    x += xinc
    y += yinc

plt.scatter(X, Y)
plt.plot(X, Y)
plt.grid()
plt.axis("equal")
plt.show()
