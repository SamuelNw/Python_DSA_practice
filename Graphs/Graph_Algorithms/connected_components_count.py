"""
Return the number of connected components.
"""

from blueprint import uc_graph


def count_connected_components(graph: dict) -> int:
    visited = set()
    count = 0

    for key in graph:
        if (explore(graph, key, visited)) == True:
            count += 1

    return count


def explore(g: dict, src: int, visited: set) -> bool:
    if src in visited:
        return False

    visited.add(src)

    for neighbor in g[src]:
        explore(g, neighbor, visited)

    return True


print(count_connected_components(uc_graph))     # --> 3
