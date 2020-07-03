from utils.m_parser import args


class Cst:
    N = args.len
    WIDTH = 700
    HEIGHT = 700
    SQUARE_SIZE = WIDTH / N
    OFFSET = 2
    DIM = (WIDTH + ((N - 1) * 2), HEIGHT + ((N - 1) * 2))
