"""Case-study #6 Tessellation
Developer:
Balabanov M.A.

"""
import ru_local as local
from turtle import *
from math import sqrt


def get_num_hexagons():
    """Hexagons quantity"""
    try:
        count = int(input(local.ROW))
        if 3 < count < 21:
            return count
        else:
            print(local.ERROR2, end="")
            return get_num_hexagons()
    except ValueError:
        print(local.ERROR2, end="")
        return get_num_hexagons()