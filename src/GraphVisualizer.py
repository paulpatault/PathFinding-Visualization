from pathfinder.Graph import Graph
from pathfinder.Algorithms import Dijkstra
from pathfinder.Algorithms import AStar
from pathfinder.Algorithms import Algorithm
from utils.m_parser import args


algorithm = AStar()
if args.algo == "dijkstra" or args.algo == "dij":
    algorithm = Dijkstra()


class GraphVisualizer:
    def __init__(self, graph: Graph, screen, table, algo: Algorithm = algorithm):
        self.graph = graph
        self.algo = algo
        self.table = table
        self.screen = screen

    def run(self, source, dest):
        return self.algo.run(self.graph, source, dest, self.screen, self.table)
