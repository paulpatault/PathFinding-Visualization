import pygame
from Table import Table
from constants import Colors
from constants import Cst
from constants import Mouse
from utils import getMousePos
from pathfinder.node import Node

pygame.init()


def main(table):
    last_mouse = Mouse(None, None)
    path = None

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            current_mouse = getMousePos()
            x, y = current_mouse

            if pygame.mouse.get_pressed()[0] and last_mouse != current_mouse:
                last_mouse = current_mouse
                table.swap(x, y)

            # clear
            if keys[pygame.K_c]:
                table.clear()
                table.setSource()
                table.setEnd()

            # set start node
            if keys[pygame.K_b]:
                source = Node(x, y)
                table.setSource(source)

            # set end node
            if keys[pygame.K_e]:
                end = Node(x, y)
                table.setEnd(end)

            # store table
            if keys[pygame.K_s]:
                table.storeBoard()

            # load stored table
            if keys[pygame.K_l]:
                table.loadBoard()

        # RUN ALGO
        if keys[pygame.K_RIGHT]:
            from GraphVisualizer import GraphVisualizer
            from pathfinder.graph import Graph
            from pathfinder.graph import graph_from_array
            from pathfinder.algorithms import Dijkstra

            graph = Graph(graph_from_array(table.array))  # AJOUT ICI
            gvisu = GraphVisualizer(graph, screen, table)
            path = gvisu.run(table.source, table.end)
            return table, path

        table.draw(screen)
        pygame.display.update()


screen = pygame.display.set_mode(Cst.DIM)
screen.fill((0, 0, 0))
pygame.display.set_caption("PathFinding Visualizer")


table = Table(Cst.N)
table.draw(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if pygame.key.get_pressed()[pygame.K_RETURN]:
        table, path = main(table)
        table.drawPath(path, screen)

    pygame.display.update()
