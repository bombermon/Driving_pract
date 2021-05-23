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
    3 DONE
       

"""


def task_4_1():
    n = 10

    first_line = list(itr.islice(dr.gen_rectangle(), n))
    second_line = list(itr.islice(dr.gen_rectangle(), n))
    third_line = list(itr.islice(dr.gen_rectangle(), n))

    first_line = list(map(dr.tr_rotate, first_line, [10]*n, [0]*n, [math.pi/4]*n))
    second_line = list(map(dr.tr_rotate, second_line, [10] * n, [0] * n, [math.pi / 4] * n))
    third_line = list(map(dr.tr_rotate, third_line, [10] * n, [0] * n, [math.pi / 4] * n))

    first_line = list(map(dr.tr_translate, first_line, [0]*n, [5]*n))
    third_line = list(map(dr.tr_translate, third_line, [0]*n, [-5]*n))

    dr.plot(first_line)
    dr.plot(second_line)
    dr.plot(third_line)

    dr.show()
    dr.clean()


def task_4_2():
    n = 10

    first_line = list(itr.islice(dr.gen_rectangle(), n))
    second_line = list(itr.islice(dr.gen_rectangle(), n))

    first_line = list(map(dr.tr_rotate, first_line, [13]*n, [0.35]*n, [math.pi/4]*n))
    second_line = list(map(dr.tr_rotate, second_line, [13] * n, [0.5] * n, [-math.pi / 4] * n))

    first_line = list(map(dr.tr_translate, first_line, [0]*n, [5]*n))

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()


def task_4_3():
    n = 3

    first_line = list(itr.islice(dr.gen_triangle(), n))
    second_line = list(itr.islice(dr.gen_triangle(), n))

    second_line = list(map(dr.tr_symmetry, second_line, [0] * n, [1.1] * n, [1] * n, [1.1] * n))

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()


def task_6_3():
    n = 30

    first_line = list(itr.islice(dr.gen_hexagon(), n))
    second_line = list(itr.islice(dr.gen_hexagon(), n))

    first_line = list(map(dr.tr_rotate, first_line, [20]*n, [0]*n, [math.pi / 150]*n))
    second_line = list(map(dr.tr_rotate, second_line, [20] * n, [0] * n, [-math.pi / 150] * n))

    first_line = list(map(dr.tr_translate, first_line, [0]*n, [-0.5]*n))

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()

    for figure in first_line:
        second_line = list(filter(lambda x: not dr.flt_polygon_angles_inside(figure, x), second_line))

    dr.plot(first_line)
    dr.plot(second_line)

    dr.show()
    dr.clean()
