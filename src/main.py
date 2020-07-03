from utils.m_parser import args

args.load()

import pygame

pygame.init()

import Table as mtable
import utils.Constants as csts
import utils.Colors as ccolors
import utils.Mouse as mouse_mod
import GraphVisualizer as gv
import pathfinder.Graph as graph_mod
from pathfinder.Node import *


def modules_reload():
    import importlib

    importlib.reload(mtable)
    importlib.reload(csts)
    importlib.reload(ccolors)
    importlib.reload(mtable)
    importlib.reload(gv)
    importlib.reload(graph_mod)
    importlib.reload(mouse_mod)


def main(table):

    mouse = mouse_mod.Mouse(0, 0)

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
        if keys[pygame.K_RETURN]:

            graph = graph_mod.Graph(graph_mod.graph_from_array(table.array))
            gvisu = gv.GraphVisualizer(graph, screen, table)
            path = gvisu.run(table.source, table.end)
            return table, path

        table.draw(screen)
        pygame.display.update()


while not args.destroy:
    screen = pygame.display.set_mode(csts.Cst.DIM)
    screen.fill((20, 20, 20))
    pygame.display.set_caption("PathFinding Visualizer")

    table = mtable.Table(csts.Cst.N)
    table.draw(screen)

    table, path = main(table)
    table.drawPath(path, screen)
    args.load()

    modules_reload()
