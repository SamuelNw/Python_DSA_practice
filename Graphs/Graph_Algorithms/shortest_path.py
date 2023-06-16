"""
Shortest path between two nodes.
"""

import collections
from blueprint import sh_edges


def shortest_path(edges: list, src: str, dst: str) -> int:
    graph = build_graph(edges)
    visited = set()
    q = collections.deque()

    visited.add(src)
    q.append([src, 0])

    while q:
        current, distance = q.popleft()
        if current == dst:
            return distance

        for neighbor in graph[current]:
            if not neighbor in visited:
                q.append([neighbor, distance + 1])
                visited.add(neighbor)

    return -1


def build_graph(lst: list) -> dict:
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


print(shortest_path(sh_edges, "W", "Z"))  # -> 2
