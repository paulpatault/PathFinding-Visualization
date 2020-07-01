from pathfinder.graph import Graph
from pathfinder.algorithms import Dijkstra
from pathfinder.algorithms import AStar


class GraphVisualizer:
    def __init__(self, graph: Graph, screen, table, algo=AStar()):
        self.graph = graph
        self.algo = algo
        self.table = table
        self.screen = screen

    def run(self, source, dest):
        return self.algo.run(self.graph, source, dest, self.screen, self.table)
