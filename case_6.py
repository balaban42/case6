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


def colors(colors_lst):
    """Colors list"""
    print(local.COLOR)
    for col in colors_lst:
        print('', col)


def draw(color1, color2, count):
    """Drawing all hexagons"""
    side_len = float(sqrt(4 * (500 / (2 * count)) ** 2 / 3))
    speed(0)
    y = 250
    x = -250
    line = 1
    for lines in range(count):
        up()
        for hexagons in range(count):
            fillcol = color1
            draw_hexagon(x, y, side_len, fillcol)
            x = xcor() + sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2
            color1, color2 = color2, color1
        if count % 2:
            color1, color2 = color2, color1
        if line % 2:
            j = 1
        else:
            color1, color2 = color2, color1
            j = 3
        y = ycor() - 3 * side_len / 2
        x = xcor() - (count * 2 - j) * sqrt(side_len ** 2 - (side_len / 2) ** 2)
        goto(x, y)
        line += 1
    done()


def main():
    colors_lst = [local.RED, local.ORANGE, local.YELLOW, local.GREEN, local.BLUE1, local.BLUE2, local.PURPLE]
    colors(colors_lst)
    color1 = get_color_choice()
    color2 = get_color_choice()
    count = get_num_hexagons()
    screensize(500, 500)
    draw(color1, color2, count)


if __name__ == '__main__':
    main()
