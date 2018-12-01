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


def get_color_choice():
    """Filling color"""
    colors_lst = [local.RED, local.ORANGE, local.YELLOW, local.GREEN, local.BLUE1, local.BLUE2, local.PURPLE]
    codes = ['#FF0000', '#FFA500', '#FFFF00', '#00FF00', '#87CEEB', '#0000FF', '#800080']
    color = str(input(local.IN_COLOR)).strip()
    color = color.lower()
    error_string = "'" + color + "' " + local.ERROR
    for i in range(7):
        if color == colors_lst[i]:
            return codes[i]
    while True:
        color = str(input(error_string))
        for i in range(7):
            if color == colors_lst[i]:
                return codes[i]


def draw_hexagon(x, y, side_len, fillcol):
    """Hexagon drawing"""
    goto(x, y)
    fillcolor(fillcol)
    down()
    s = 0
    begin_fill()
    right(30)
    while s < 600:
        forward(side_len)
        right(60)
        s += 120
    forward(side_len)
    right(30)
    end_fill()
    up()