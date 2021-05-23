import driving as dr
import itertools
import math

""" TODO list, 13 left
5:
    1 convex polygon DONE
    2 angle point DONE  
    3 square DONE
    4 short side DONE
    5 point inside DONE
    6 polygon angles inside DONE
    

7:
    1
    2
    
8:
    1 origin nearest DONE
    2 max side DONE
    3 min area DONE
    4 perimeter DONE
    5 area DONE

2:
    4
    
4:
    1
    2
    3
    4
    
6:
    выберем
       

"""

a = tuple(itertools.islice(dr.gen_triangle(), 2))
b =  tuple(itertools.islice(dr.gen_hexagon(), 3))
c = tuple(itertools.islice(dr.gen_rectangle(), 2))
#a = tuple(map(dr.tr_symmetry, a, [0]*len(a), [0]*len(a), [1]*len(a), [1]*len(a)))
#c = [((0, 0), (0, 1), (1, 1)), ((2, 0), (2, 1), (3, 1))]
#b = tuple(filter(lambda x: dr.flt_angle_point(x, (0, 0)), c))
dr.plot(a)
dr.plot(b)
dr.plot(c)
dr.show()
