from collections import namedtuple
from pathfinder.node import Node

Edge = namedtuple("Edge", "start, end, cost")


def make_edge(start: Node, end: Node, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        self.edges = [make_edge(*edge) for edge in edges]
        self.vertices = self._vertices()
        self.neighbours = self._neighbours()

    # @property
    def _vertices(self):
        return set(sum(([edge.start.id, edge.end.id] for edge in self.edges), []))

    # @property
    def _neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start.id].add((edge.end.id, edge.cost))
        return neighbours

    def __str__(self):
        return str(self.neighbours)

    def remove_edge(self, n1, n2):
        node_pairs = [[n1, n2], [n2, n1]]
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

        self.vertices = self._vertices()
        self.neighbours = self._neighbours()

    def add_edge(self, n1, n2, cost=1):
        node_pairs = [[n1, n2], [n2, n1]]
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError(f"Edge {n1} {n2} already exists")

        self.edges.append(Edge(n1, n2, cost))
        self.edges.append(Edge(n2, n1, cost))

        self.vertices = self._vertices()
        self.neighbours = self._neighbours()


def graph_from_array(arr):
    def is_valid(pos):
        from utils.constants import Cst

        x, y = pos

        if x >= 0 and y >= 0 and x < Cst.N and y < Cst.N:
            return arr[x][y] != 1

        return False

    def direct_neighbours(node: Node):
        neighbours = []
        l = [
            (-1, -1, 1.4),
            (0, -1, 1),
            (1, -1, 1.4),
            (-1, 0, 1),
            (1, 0, 1),
            (-1, 1, 1.4),
            (0, 1, 1),
            (1, 1, 1.4),
        ]

        for x, y, w in l:
            pos = (node.x + x, node.y + y)
            if is_valid(pos):
                n = (Node(*pos), w)
                neighbours.append(n)

        return neighbours

    edges = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 1:
                node = Node(i, j)
                neighbours = direct_neighbours(node)
                for n in neighbours:
                    edge = (node, *n)
                    a, b = n
                    # print(f"{node.id} -> {a.id}_{b}")
                    edges.append(edge)
            # else:
            #    print(i, j)
    return edges

