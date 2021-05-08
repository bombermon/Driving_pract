def inPolygon(x, y, figure):
    figure = ((0, 0), (0, 1), (1, 1))
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


print(inPolygon(0.8, 0.2))