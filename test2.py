import driving as dr
import functools as ft
from functools import reduce

"""tirangle1 = ((0, 0), (0, 1), (1, 1))
print(dr.flt_short_side(tirangle1, 0.3))"""
figures = [((0, 1), (0, 1), (1, 1), (1, 0)), ((0, 0), (0, 1), (1, 1), (1, 0))]
print(reduce(dr.agr_min_area, figures, 999))

