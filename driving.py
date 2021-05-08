import matplotlib.pyplot as plt
import math


# НАЧАЛО ВСПОМОГАТЕЛЬНЫХ ------------------------------------------------------------------------------

def get_length(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def get_triangle_area(point1, point2, point3):
    a, b, c = get_length(point1, point2), get_length(point2, point3), get_length(point3, point1)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def get_any_area(figure):
    n = len(figure)
    plus = 0
    minus = 0
    for i in range(0, n):
        x1 = figure[i][0]
        y2 = figure[(i + 1) % n][1]
        x2 = figure[i][1]
        y1 = figure[(i + 1) % n][0]
        plus += x1 * y2
        minus += x2 * y1

    s = abs(plus - minus) / 2
    return s


# КОНЕЦ ВСПОМОГАТЕЛЬНЫХ -------------------------------------------------------------------------------


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


def tr_homothety(figure, x0, y0, k):
    result_figure = []
    for i in figure:
        x = i[0]
        y = i[1]
        new_vector = [(x - x0) * k, (y - y0) * k]
        new_koords = (new_vector[0] + x0, new_vector[1] + y0)
        result_figure.append((new_koords))
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


def flt_angle_point(figure, point):
    for i in figure:
        if i[0] == point[0] and i[1] == point[1]:
            return True
    return False


def flt_square(figure, area):
    cur_area = get_any_area(figure)

    if cur_area < area:
        return True
    else:
        return False


def flt_short_side(figure, side):
    n = len(figure)
    for i in range(n):
        current_side = get_length(figure[i], figure[(i + 1) % n])
        if current_side < side:
            return True
    return False


def flt_point_inside(x, y, figure):
    c = 0
    for i in range(len(figure)):
        if (((figure[i][1] <= y and y < figure[i - 1][1]) or (figure[i - 1][1] <= y and y < figure[i][1])) and
                (x > (figure[i - 1][0] - figure[i][0]) *
                 (y - figure[i][1]) / (figure[i - 1][1] - figure[i][1]) + figure[i][0])):
            c = 1 - c
    if c == 0:
        return False
    elif c == 1:
        return True


def flt_convex_polygon(figure):
    def cross_product(a, b, c):
        return (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])

    n = len(figure)
    if n < 4:
        return True

    found_direction = False
    clockwise_direction = False

    for i in range(n):
        current_cross_product = cross_product(figure[i], figure[(i + 1) % n], figure[(i + 2) % n])
        if current_cross_product != 0:
            if not found_direction:
                found_direction = True
                if current_cross_product < 0:
                    clockwise_direction = True
            else:
                current_clockwise_direction = current_cross_product < 0
                if current_clockwise_direction != clockwise_direction:
                    return False

    return True


def flt_polygon_angles_inside(figure, figure_to_cheek):
    for i in figure_to_cheek:
        if flt_point_inside(figure, i):
            return True
    return False


def plot(a):
    b = tuple(a)
    for i in b:
        for j in range(len(i)):
            if j != len(i) - 1:
                plt.plot((i[j][0], i[j + 1][0]), (i[j][1], i[j + 1][1]), color="black")
            else:
                plt.plot((i[j][0], i[0][0]), (i[j][1], i[0][1]), color="black")


def clean():
    plt.clf()


def show():
    plt.show()
