"""
Checking whether there exists a path that connects 'source' and 'destination'.
"""

from blueprint import graph_d

# check path in directed graph


def has_path(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True

    return False


print(has_path(graph_d, "A", "F"))  # --> True
