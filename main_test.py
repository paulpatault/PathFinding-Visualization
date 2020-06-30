from pathfinder.graph import Graph, graph_from_array
from pathfinder.algorithms import dijkstra


# Test 1

graph = Graph(
    [
        ("a", "b"),
        ("a", "c"),
        ("a", "f"),
        ("b", "c"),
        ("b", "d"),
        ("c", "d"),
        ("c", "f"),
        ("d", "e"),
        ("e", "f"),
    ]
)
print(dijkstra(graph, "a", "e"))


# Test 2

arr = [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]
graph = graph_from_array(arr)
print(dijkstra(graph, 0, 12))
