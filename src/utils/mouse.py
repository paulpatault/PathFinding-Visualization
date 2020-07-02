import pygame
from utils.Constants import Cst

if not pygame.get_init():
    pygame.init()

"""
class Mouse:
    def __init__(self, x, y):
        self.current = (x, y)
        self.last = (-1, -1)

    @property
    def moved_case(self):
        print(self.current, self.last)
        return self.current != self.last

    def used(self):
        # print("used")
        self.last = self.current

    def get_pos(self):
        return self.current

    def set_current(self, x, y):
        self.current = (x, y)

    def update(self):
        x, y = pygame.mouse.get_pos()
        x = int(x / (Cst.SQUARE_SIZE + Cst.OFFSET))
        y = int(y / (Cst.SQUARE_SIZE + Cst.OFFSET))

        self.set_current(x, y)
        if self.moved_case:
            self.used()
"""


class Mouse:
    def __init__(self, x, y):
        self.current = (x, y)
        self.last = (-1, -1)
        self.moved_case = True
        self.used = False

    @property
    def usable(self):
        return self.moved_case

    def released(self):
        self.used = False

    def use(self):
        self.last = self.current
        self.used = True

    def get_pos(self):
        return self.current

    def set_current(self, x, y):
        self.current = (x, y)

    def update(self):
        x, y = pygame.mouse.get_pos()
        x = int(x / (Cst.SQUARE_SIZE + Cst.OFFSET))
        y = int(y / (Cst.SQUARE_SIZE + Cst.OFFSET))

        self.set_current(x, y)

        if self.last != self.current:
            self.moved_case = True
            self.used = False
        elif self.used:
            self.moved_case = False
