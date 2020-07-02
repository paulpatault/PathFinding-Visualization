import pygame
from Table import Table
from utils.Constants import *
from utils.Colors import Colors
from utils.Mouse import Mouse
from pathfinder.Node import Node

pygame.init()


def main(table):

    mouse = Mouse(0, 0)

    while True:
        keys = pygame.key.get_pressed()

        mouse.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.mouse.get_pressed()[0] and mouse.usable:
                mouse.use()
                x, y = mouse.get_pos()
                table.swap(x, y)

            if not pygame.mouse.get_pressed()[0]:
                mouse.released()

            # clear
            if keys[pygame.K_c]:
                table.clear()
                table.setSource()
                table.setEnd()

            # set start node
            if keys[pygame.K_b]:
                x, y = mouse.get_pos()
                source = Node(x, y)
                table.setSource(source)

            # set end node
            if keys[pygame.K_e]:
                x, y = mouse.get_pos()
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
            from pathfinder.Graph import Graph
            from pathfinder.Graph import graph_from_array

            graph = Graph(graph_from_array(table.array))
            gvisu = GraphVisualizer(graph, screen, table)
            path = gvisu.run(table.source, table.end)
            return table, path

        table.draw(screen)
        pygame.display.update()


screen = pygame.display.set_mode(Cst.DIM)
screen.fill((20, 20, 20))
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
