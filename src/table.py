import pygame
import pickle
from utils.Colors import Colors
from utils.Constants import Cst
from pathfinder.Node import Node


class Table:
    path_is_draw = False
    """
    0: empty
    1: wall
    2: visited
    3: openset
    10: path
    """

    def __init__(self, n):
        self.array = [[0 for i in range(n)] for j in range(n)]
        self.n = n

        self.source = Node(0, 0)
        self.end = Node(self.n - 1, self.n - 1)

        self.setSource()
        self.setEnd()

    def setSource(self, source=None):
        """
        source : Node
        Set self.source to source.
        Reset if source == None
        """
        i, j = self.source.id
        self.array[i][j] = 0
        if source:
            i, j = source.id
            self.array[i][j] = 4
            self.source = source
        else:
            self.array[0][0] = 4
            self.source = Node(0, 0)

    def setEnd(self, end=None):
        """
        end : Node
        Set self.end to end.
        Reset if end == None
        """
        i, j = self.end.id
        self.array[i][j] = 0
        if end:
            i, j = end.id
            self.array[i][j] = 5
            self.end = end
        else:
            self.array[self.n - 1][self.n - 1] = 5
            self.end = Node(self.n - 1, self.n - 1)

    def swap(self, i, j):
        """
        i, j : coordonées  
        Set self.array[i][j] to 1 (wall) if empty,
        empty self.array[i][j] (to 0) if it's a wall.
        """
        if self.array[i][j] == 0:
            self.array[i][j] = 1
        else:
            self.array[i][j] = 0

    def __notSourceOrEnd(self, i, j):
        return (i, j) not in [self.source.id, self.end.id]

    def setVisited(self, i, j):
        """
        i, j : coordonées  
        Set self.array[i][j] to 2 (visited).
        """
        if self.__notSourceOrEnd(i, j):
            self.array[i][j] = 2

    def setOpenSet(self, i, j):
        """
        i, j : coordonées  
        Set self.array[i][j] to 3 (openset) if it is not visited.
        """
        if self.__notSourceOrEnd(i, j) and self.array[i][j] != 2:
            self.array[i][j] = 3

    def __makeRect(self, i, j, state):
        rect = pygame.Rect(
            i * (Cst.SQUARE_SIZE + Cst.OFFSET),
            j * (Cst.SQUARE_SIZE + Cst.OFFSET),
            Cst.SQUARE_SIZE,
            Cst.SQUARE_SIZE,
        )
        color = Colors(state).rgb

        if state == 3:
            alpha = 0.85
            dem_alpha = (1 - alpha) / 2
            rect = pygame.Rect(
                i * (Cst.SQUARE_SIZE + Cst.OFFSET)
                + ((Cst.SQUARE_SIZE + 4 * Cst.OFFSET) * dem_alpha),
                j * (Cst.SQUARE_SIZE + Cst.OFFSET)
                + ((Cst.SQUARE_SIZE + 4 * Cst.OFFSET) * dem_alpha),
                Cst.SQUARE_SIZE * alpha,
                Cst.SQUARE_SIZE * alpha,
            )

        return (color, rect)

    def draw(self, screen):
        """
        Display the instance of the Table
        """
        for i, arr in enumerate(self.array):
            for j, e in enumerate(arr):
                pygame.draw.rect(screen, *self.__makeRect(i, j, e))

        pygame.display.update()

    def setPath(self, path, screen):
        """
        path : list of node.id
        Set to 10 (path) every node to represent the path in self.array
        """
        if not path:
            return False
        for (i, j) in path:
            if self.__notSourceOrEnd(i, j):
                pygame.time.delay(20)
                self.array[i][j] = 10
                pygame.draw.rect(screen, *self.__makeRect(i, j, 10))
                pygame.display.update()
        return True

    def drawPath(self, path, screen):
        """
        path : list of node.id
        Draw the path given in parameter
        """
        if self.setPath(path, screen):
            self.draw(screen)
            self.path_is_draw = True

    def clear(self):
        """
        Clear the path if it is draw, clear walls other in the other case.
        """
        if self.path_is_draw:
            for i in range(self.n):
                for j in range(self.n):
                    if self.array[i][j] != 1:
                        self.array[i][j] = 0
            self.path_is_draw = False
        else:
            self.array = [[0 for i in range(self.n)] for j in range(self.n)]

    def storeBoard(self):
        """
        Store the actual board in bytes in the file 'board.data' with pickle 
        """
        with open("board.data", "wb") as file:
            pickle.dump(self.array, file)

    def loadBoard(self):
        """
        Load stored board in the file 'board.data'
        """
        with open("board.data", "rb") as file:
            array = pickle.load(file)
            self.array = array

