import matplotlib.pyplot as plt

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
        yield (0 + counter * n, 0.5), (0.25 + counter * n, 0.067), (0.75 + counter * n, 0.067), (1 + counter * n, 0.5), (0.75 + counter * n, 1-0.067), (0.25 + counter * n, 1-0.067)
        counter += 1

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



