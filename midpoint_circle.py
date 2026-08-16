import matplotlib.pyplot as plt

xc, yc = map(int, input("Enter center xc yc: ").split())
r = int(input("Enter radius: "))

x, y = 0, r
p = 1 - r

X, Y = [], []

while x <= y:

    points = [(x,y), (-x,y), (x,-y), (-x,-y),
              (y,x), (-y,x), (y,-x), (-y,-x)]

    for a, b in points:
        X.append(xc + a)
        Y.append(yc + b)

    x += 1

    if p < 0:
        p += 2*x + 1
    else:
        y -= 1
        p += 2*(x-y) + 1

plt.scatter(X, Y)
plt.axis("equal")
plt.grid()
plt.show()