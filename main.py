import driving as dr
import itertools as itr
import math

""" TODO list, 13 left
5:
    1 convex polygon DONE
    2 angle point DONE  
    3 square DONE
    4 short side DONE
    5 point inside DONE
    6 polygon angles inside DONE
    
    
8:
    1 origin nearest DONE
    2 max side DONE
    3 min area DONE
    4 perimeter DONE
    5 area DONE

2:
    4
    
4:
    1 DONE
    2 DONE
    3 DONE
    4
    
6:
    выберем
       

"""


def task_2_1():
    fig = tuple(itr.islice(dr.gen_rectangle(), 10))
    dr.plot(fig)
    dr.show()


def task_2_2():
    fig = tuple(itr.islice(dr.gen_triangle(), 10))
    dr.plot(fig)
    dr.show()


def task_2_3():
    fig = tuple(itr.islice(dr.gen_hexagon(), 10))
    dr.plot(fig)
    dr.show()


def task_2_4():
    a = tuple(itr.islice(dr.gen_triangle(), 2))
    b = tuple(itr.islice(dr.gen_hexagon(), 3))
    c = tuple(itr.islice(dr.gen_rectangle(), 2))
    dr.plot(a)
    dr.plot(b)
    dr.plot(c)
    dr.show()


def task_3_1():
    fig = tuple(itr.islice(dr.gen_triangle(), 10))
    n = len(fig)
    fig1 = tuple(map(dr.tr_translate, fig, [5] * n, [5] * n))
    dr.plot(fig)
    dr.plot(fig1)
    dr.show()


def task_3_2():
    fig = tuple(itr.islice(dr.gen_triangle(), 10))
    n = len(fig)
    fig1 = tuple(map(dr.tr_rotate, fig, [0] * n, [0] * n, [2] * n))
    dr.plot(fig)
    dr.plot(fig1)
    dr.show()


def task_3_3():
    fig = tuple(itr.islice(dr.gen_triangle(), 10))
    n = len(fig)
    fig1 = tuple(map(dr.tr_symmetry, fig, [0] * n, [0] * n, [-1] * n, [0] * n))
    dr.plot(fig)
    dr.plot(fig1)
    dr.show()


def task_3_4():
    fig = tuple(itr.islice(dr.gen_triangle(), 10))
    n = len(fig)
    fig1 = tuple(map(dr.tr_homothety, fig, [0] * n, [0] * n, [-1] * n))
    dr.plot(fig)
    dr.plot(fig1)
    dr.show()

def task_4_1():
    n = 10

    first_line = list(itr.islice(dr.gen_rectangle(), n))
    second_line = list(itr.islice(dr.gen_rectangle(), n))
    third_line = list(itr.islice(dr.gen_rectangle(), n))

    first_line = map(dr.tr_rotate, first_line, [10]*n, [0]*n, [math.pi/4]*n)
    second_line = map(dr.tr_rotate, second_line, [10] * n, [0] * n, [math.pi / 4] * n)
    third_line = map(dr.tr_rotate, third_line, [10] * n, [0] * n, [math.pi / 4] * n)

    first_line = map(dr.tr_translate, first_line, [0]*n, [5]*n)
    third_line = map(dr.tr_translate, third_line, [0]*n, [-5]*n)

    dr.plot(first_line)
    dr.plot(second_line)
    dr.plot(third_line)

    dr.show()
    dr.clean()


def task_4_2():
    n = 10

    first_line = list(itr.islice(dr.gen_rectangle(), n))
    second_line = list(itr.islice(dr.gen_rectangle(), n))

    first_line = map(dr.tr_rotate, first_line, [13]*n, [0.35]*n, [math.pi/4]*n)
    second_line = map(dr.tr_rotate, second_line, [13] * n, [0.5] * n, [-math.pi / 4] * n)

    first_line = map(dr.tr_translate, first_line, [0]*n, [5]*n)

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()


def task_4_3():
    n = 3

    first_line = list(itr.islice(dr.gen_triangle(), n))
    second_line = list(itr.islice(dr.gen_triangle(), n))

    second_line = map(dr.tr_symmetry, second_line, [0] * n, [1.1] * n, [1] * n, [1.1] * n)

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()



def task_4_4():
    fig = tuple(itr.islice(dr.gen_rectangle(), 10))
    n = len(fig)
    fig = tuple(map(dr.tr_rotate, fig, [0] * n, [0] * n, [math.pi / 4] * n))
    fig1 = tuple(map(dr.tr_homothety, fig, [0] * n, [0] * n, [2] * n))
    fig1 = tuple(map(dr.tr_symmetry, fig1, [0] * n, [0] * n, [-1] * n, [1] * n))
    dr.plot(fig)
    dr.plot(fig1)
    dr.show()


task_4_4()
