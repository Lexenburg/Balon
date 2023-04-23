from math import *
import matplotlib as mpl
import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera


def Peplin(y):
    y -= np.array([y[0] + y[2] * cos(3.0 * np.pi / 2.0 - y[3]) - Ax,
                   y[1] + y[5] * cos(3.0 * np.pi / 2.0 + y[4]) - Bx,
                   y[2] + y[2] * sin(3.0 * np.pi / 2.0 - y[3]) - Ay,
                   (y[3] + y[4]) * y[2] + (y[1] - y[0]) - C,
                   y[2] + y[2] * sin(3.0 * np.pi / 2.0 + y[4]) - By,
                   y[2] + y[2] * sin(3.0 * np.pi / 2.0 - y[3]) - Ay]) * tao
    return y


def lexa(y):
    return y - np.array([y[0] + y[2] * cos(3.0 * np.pi / 2.0 - y[3]) - Ax,
                         y[1] + y[5] * cos(3.0 * np.pi / 2.0 + y[4]) - Bx,
                         y[2] + y[2] * sin(3.0 * np.pi / 2.0 - y[3]) - Ay,
                         y[3] + (y[4] * y[5] + (y[1] - y[0]) - C)/y[2],
                         y[4] + (y[3] * y[2] + (y[1] - y[0]) - C)/y[5],
                         y[5] + y[5] * sin(3.0 * np.pi / 2.0 + y[4]) - By]) * tao


it_cnt = 5000
tao = 0.005
delta_t = 0.01
m = 100.0
p = 2000.0
g = 9.8
Vy = 0.0
Ax, Bx, Ay, By, C = -0.353, 0.353, 0.3, 0.3, 3.0 * np.pi / 8.0
x = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])  # x1, x2, y1, phi1, phi2, y2

fig, axes = plt.subplots()
axes.set_aspect("equal")

plt.grid()
plt.xlim(-0.5, 0.5)
plt.ylim(-0.1, 0.9)

camera = Camera(fig)

for j in range(0, 250):
    Vy += (p * (x[1] - x[0]) - m * g) / m * delta_t
    Ay += Vy * delta_t
    By = Ay

    for i in range(it_cnt):
        x = lexa(x)
        # print(x)
    # print(x)

    plt.grid()
    plt.xlim(-0.5, 0.5)
    plt.ylim(-0.1, 0.9)

    axes = plt.gca()
    axes.set_aspect("equal")

    h1 = 2 * x[2]
    h2 = 2 * x[5]
    arc1 = mpl.patches.Arc((x[0], x[2]), h1, h1, theta1=(270.0 - x[3] * 180.0 / np.pi), theta2=270.0, color='pink')
    arc2 = mpl.patches.Arc((x[1], x[5]), h2, h2, theta1=270.0, theta2=270.0 + x[4] * 180.0 / np.pi, color='pink')

    plt.plot([Ax, Bx], [Ay, By], color='pink')
    # plt.plot(x[1], x[5], 'ro')
    plt.plot([x[0], x[1]], [0, 0], color='pink')
    axes.add_patch(arc1)
    axes.add_patch(arc2)
    # print(x[3] * x[2] + x[1] - x[0] + x[4] * x[5])

    camera.snap()
animation = camera.animate()
plt.show()
