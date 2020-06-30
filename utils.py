def calculateIJFromV(v, N):
    i = 0
    while v >= N:
        i += 1
        v -= N
    return (i, v)


def calculateIJsFromV(v, N):
    res = []
    for e in v:
        res.append(calculateIJFromV(e, N))
    return res


def getMousePos():
    import pygame
    from constants import Cst
    from constants import Mouse

    if not pygame.get_init():
        pygame.init()

    x, y = pygame.mouse.get_pos()
    x = int(x / (Cst.SQUARE_SIZE + Cst.OFFSET))
    y = int(y / (Cst.SQUARE_SIZE + Cst.OFFSET))
    return Mouse(x, y)
