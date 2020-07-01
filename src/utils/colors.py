from enum import Enum


class Colors(bytes, Enum):
    """
    
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
