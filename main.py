import driving as dr
import itertools
import math

a = tuple(itertools.islice(dr.gen_rectangle(), 13))
a = tuple(map(dr.tr_homothety, a, [5]*len(a), [5]*len(a), [1]*len(a)))
print(a)
dr.plot(a)
dr.show()
