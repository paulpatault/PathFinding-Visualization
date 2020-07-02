from enum import Enum
from utils.m_parser import args

strong = args.C == "strong"


class Colors(bytes, Enum):
    """
    
    """

    def __new__(cls, value, rgb):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.rgb = rgb
        return obj

    if not strong:
        SMOOTH_BACKGROUND = (0, (140, 140, 140))
        SMOOTH_WALL = (1, (0, 0, 0))
        SMOOTH_VISITED = (2, (203, 203, 203))
        SMOOTH_OPENSET = (3, (255, 238, 95))
        SMOOTH_SOURCE_NODE = (4, (245, 119, 119))
        SMOOTH_END_NODE = (5, (212, 119, 245))
        SMOOTH_PATH = (10, (127, 182, 243))
    else:
        STRONG_BACKGROUND = (0, (255, 255, 255))
        STRONG_WALL = (1, (0, 0, 0))
        STRONG_VISITED = (2, (135, 245, 119))
        STRONG_OPENSET = (3, (150, 190, 240))
        STRONG_SOURCE_NODE = (4, (245, 119, 119))
        STRONG_END_NODE = (5, (212, 119, 245))
        STRONG_PATH = (10, (255, 245, 85))
