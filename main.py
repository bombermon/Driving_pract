import driving as dr
import itertools
import math

""" TODO list, 18 left
5:
    1 convex polygon Rusik
    2 angle point DONE  
    3 square DONE
    4 short side DONE
    5 point inside Vovasik
    6
    

7:
    1
    2
    
8:
    1
    2
    3
    4
    5

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

#a = tuple(itertools.islice(dr.gen_triangle(), 3))
#a = tuple(map(dr.tr_symmetry, a, [0]*len(a), [0]*len(a), [1]*len(a), [1]*len(a)))
c = [((0, 0), (0, 1), (1, 1))]
#b = tuple(filter(lambda x: dr.flt_angle_point(x, (0, 0)), c))
dr.plot(c)
#dr.plot(b)
dr.show()
