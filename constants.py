from enum import Enum


class Colors(bytes, Enum):
    """
    Coordinate with binary codes that can be indexed by the int code.
    """

    def __new__(cls, value, rgb):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.rgb = rgb
        return obj

    WHITE = (0, (255, 255, 255))
    WALL = (1, (0, 0, 0))
    VISITED = (2, (135, 245, 119))
    OPENSET = (3, (150, 190, 240))
    SOURCE_NODE = (4, (245, 119, 119))
    END_NODE = (5, (212, 119, 245))
    YELLOW = (10, (255, 245, 85))


class Colors__:
    BLUE = (150, 190, 240)
    GREEN = (135, 245, 119)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 245, 85)

    SOURCE_NODE = (245, 119, 119)
    END_NODE = (212, 119, 245)

    def getColor(case):
        if case == 0:
            return Colors.WHITE
        if case == 1:
            return Colors.BLACK
        if case == 2:
            return Colors.GREEN
        if case == 3:
            return Colors.BLUE
        if case == 10:
            return Colors.YELLOW
        if case == 4 or case == "source":
            return Colors.SOURCE_NODE
        if case == 5 or case == "end":
            return Colors.END_NODE


class Cst:
    N = 30
    WIDTH = 700
    HEIGHT = 700
    SQUARE_SIZE = WIDTH / N
    OFFSET = 2
    DIM = (WIDTH + ((N - 1) * 2), HEIGHT + ((N - 1) * 2))


from collections import namedtuple

Mouse = namedtuple("Mouse", "x, y")
