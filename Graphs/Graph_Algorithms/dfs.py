"""
DFS graph Traversal implementation.
"""

from blueprint import graph_d


# Basic directed graph dfs traversal.
def iterative_dfs(g: dict, source: str):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbor in g[current]:
            stack.append(neighbor)


def recursive_dfs(g: dict, source: str):
    print(source)

    for neighbor in g[source]:
        recursive_dfs(g, neighbor)


iterative_dfs(graph_d, "A")  # --> ACEBDF
print("***** recursive: *****")
recursive_dfs(graph_d, "A")  # --> ABDFCE
