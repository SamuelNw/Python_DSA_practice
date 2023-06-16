"""
BFS graph Traversal implementation.
"""

import collections
from blueprint import graph_d


def bfs(g, source):
    q = collections.deque()
    q.append(source)

    while q:
        current = q.popleft()
        print(current)

        for neighbor in g[current]:
            q.append(neighbor)


bfs(graph_d, "A")   # ---> ABCDEF
