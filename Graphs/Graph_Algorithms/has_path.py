"""
Checking whether there exists a path that connects 'source' and 'destination'.
"""

import collections
from blueprint import graph_d

# check path in directed graph --> dfs


def has_path(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True

    return False


# bfs way:
def has_path_bfs(graph, src, dst):
    q = collections.deque()
    q.append(src)

    while q:
        current = q.popleft()
        if current == dst:
            return True

        for neighbor in graph[current]:
            q.append(neighbor)

    return False


print(has_path(graph_d, "A", "F"))  # --> True
print(has_path_bfs(graph_d, "A", "F"))  # --> True
