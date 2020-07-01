from pathfinder.graph import Graph
from pathfinder.node import Node

from Table import Table

import math


class Algorithm:
    def __init__(self):
        pass

    def run(self, graph: Graph, source, dest, screen, table: Table):
        pass


class Dijkstra(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)

    def run(self, graph: Graph, source, dest, screen, table: Table):
        assert source in graph.vertices, "Such source node doesn't exist"
        if source == dest:
            return None
        inf = float("inf")
        distances = {vertex: inf for vertex in graph.vertices}
        previous_vertices = {vertex: None for vertex in graph.vertices}
        distances[source] = 0
        Q = graph.vertices.copy()

        while Q:
            current_vertex = min(Q, key=lambda vertex: distances[vertex])

            if current_vertex == dest:
                break
            # (i, j) = calculateIJFromV(current_vertex, Cst.N)
            table.array[i][j] = 2
            table.draw(screen)

            Q.remove(current_vertex)
            for neighbour, cost in graph.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = [], dest
        while previous_vertices[current_vertex]:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(current_vertex)
        path.append(source)

        path = path[::-1]
        return path


class AStar(Algorithm):
    dest = None

    def __init__(self):
        Algorithm.__init__(self)

    def _euclidian(self, i, j):
        x, y = self.dest
        return math.sqrt(abs(x - i) ** 2 + abs(y - j) ** 2)

    def heuristic(self, p):
        if type(p) is tuple:
            return self._euclidian(*p)
        else:
            return self._euclidian(*p.id)

    def reconstruct_path(self, previous_vertices, current_vertex):
        path = []
        while previous_vertices[current_vertex]:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(current_vertex)

        return path[::-1]

    def run(self, graph: Graph, source, dest, screen, table: Table):
        self.dest = dest.id

        assert source.id in graph.vertices, "Such source node doesn't exist"
        if source == dest:
            return None

        previous_vertices = {vertex: None for vertex in graph.vertices}

        inf = float("inf")
        gScore = {vertex: inf for vertex in graph.vertices}
        gScore[source.id] = 0

        fScore = {vertex: inf for vertex in graph.vertices}
        fScore[source.id] = self.heuristic(source.id)

        openSet = set()

        openSet.add(source.id)

        while openSet:
            current_vertex = min(openSet, key=lambda vertex: fScore[vertex])

            if current_vertex == dest:
                return self.reconstruct_path(previous_vertices, current_vertex)

            openSet.remove(current_vertex)

            table.setVisited(*current_vertex)

            for neighbour, weight in graph.neighbours[current_vertex]:
                alternative_route = gScore[current_vertex] + weight
                if alternative_route < gScore[neighbour]:
                    gScore[neighbour] = alternative_route
                    fScore[neighbour] = gScore[neighbour] + self.heuristic(neighbour)
                    previous_vertices[neighbour] = current_vertex
                    if neighbour not in openSet:
                        openSet.add(neighbour)
                        table.setOpenSet(*neighbour)
            table.draw(screen)

        return None
