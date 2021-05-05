import driving as dr
import itertools

a = tuple(itertools.islice(dr.gen_triangle(), 10))
b = tuple(itertools.islice(dr.gen_hexagon(), 3))

dr.plot(b)
dr.show()
