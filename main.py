import driving as dr
import itertools
import math

a = tuple(itertools.islice(dr.gen_triangle(), 3))
a = tuple(map(dr.tr_symmetry, a, [0]*len(a), [0]*len(a), [1]*len(a), [1]*len(a)))
print(a)
dr.plot(a)
dr.show()
