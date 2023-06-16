"""
Check path between two nodes in an undirected graph.
"""

from blueprint import edges


def has_path(arr, source, destination):
    graph = build_graph(arr)
    return traverse(graph, source, destination, set())


def traverse(g, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)

    for neighbor in g[src]:
        if traverse(g, neighbor, dst, visited) == True:
            return True

    return False


def build_graph(lst):
    graph = {}

    for edge in lst:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


print(has_path(edges, "A", "E"))     # --> Return True
