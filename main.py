import driving as dr
import itertools
import math

a = tuple(itertools.islice(dr.gen_rectangle(), 13))
a = tuple(map(dr.tr_rotate, a, [0]*len(a), [0]*len(a), [math.pi / 3]*len(a)))
print(a)
dr.plot(a)
dr.show()
