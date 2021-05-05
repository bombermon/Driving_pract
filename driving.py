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





def show():
    a = [1, 2, 3]
    b = [1, 2, 3]
    plt.plot(a, b)
    plt.show()



