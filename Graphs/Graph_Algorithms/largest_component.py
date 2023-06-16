"""
Return the number of nodes in the largest connected component.
"""

from blueprint import uc_graph


def largest_component(graph: dict) -> int:
    visited = set()
    res = 0

    for key in graph:
        size = explore_nodes(graph, key, visited)
        res = max(res, size)

    return res


def explore_nodes(g: dict, src: int, visited: set) -> int:
    if src in visited:
        return 0

    visited.add(src)

    nodes = 1

    for neighbor in g[src]:
        nodes += explore_nodes(g, neighbor, visited)

    return nodes


print(largest_component(uc_graph))
