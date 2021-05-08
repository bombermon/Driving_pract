n = len(figure)
plus = 0
minus = 0
for i in range(0, n):
    x1 = figure[i][0]
    y2 = figure[(i+1) % n][1]
    x2 = figure[i][1]
    y1 = figure[(i+1) % n][0]
    plus += x1 * y2
    minus += x2 * y1

s = abs(plus - minus) / 2

print(s)

