import matplotlib.pyplot as plt
import math


def gen_rectangle():
    counter = 0
    while True:
        yield (0 + counter * 2, 0), (0 + counter * 2, 1), (1 + counter * 2, 1), (1 + counter * 2, 0)
        counter += 1


def gen_triangle():
    counter = 0
    while True:
        yield (0 + counter * 3, 0), (1 + counter * 3, 1), (2 + counter * 3, 0)
        counter += 1


def gen_hexagon():
    counter = 0
    while True:
        n = 2
        yield (0 + counter * n, 0.5), (0.25 + counter * n, 0.067), (0.75 + counter * n, 0.067), (
            1 + counter * n, 0.5), (0.75 + counter * n, 1 - 0.067), (0.25 + counter * n, 1 - 0.067)
        counter += 1


def tr_translate(figure, x, y):
    result_figure = []
    for i in figure:
        result_figure.append((i[0] + x, i[1] + y))
    return tuple(result_figure)


def tr_rotate(figure, x0, y0, radian):
    sin = math.sin(radian)
    cos = math.cos(radian)
    result_figure = []
    for i in figure:
        x = i[0]
        y = i[1]
        result_figure.append(((x - x0) * cos - (y - y0) * sin + x0, (x - x0) * sin + (y - y0) * cos + y0))
    return tuple(result_figure)


def tr_symmetry(figure, p1x, p1y, p2x, p2y):
    dx = p2x - p1x
    dy = p2y - p1y
    result_figure = []
    for i in figure:
        p0x = i[0]
        p0y = i[1]
        ax = (((dx * p0x + dy * p0y) * -1 * dx) - (dy * (dy * p1x - dx * p1y))) / (-1 * dx * dx - dy * dy)
        ay = ((dx * (dy * p1y - dx * p1y)) - (dy * (dx * p0x + dy * p0y))) / (-1 * dx * dx - dy * dy)
        x = ax + (ax - p0x)
        y = ay + (ay - p0y)
        result_figure.append((x, y))
    return tuple(result_figure)


def plot(a):
    plt.clf()
    b = tuple(a)
    for i in b:
        for j in range(len(i)):
            if j != len(i) - 1:
                plt.plot((i[j][0], i[j + 1][0]), (i[j][1], i[j + 1][1]), color="black")
            else:
                plt.plot((i[j][0], i[0][0]), (i[j][1], i[0][1]), color="black")


def show():
    plt.show()
