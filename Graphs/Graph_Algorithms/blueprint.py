# Undirected graph represented as an adjacency dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D'],
    'F': ['A']
}


# Directed graph represented as an adjacency dictionary
graph_d = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

# Edges for an undirected graph (cyclic)
edges = [
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'D'],
    ['D', 'E'],
    ['E', 'F'],
    ['F', 'A']
]

# Unconnected graph (undirected)
uc_graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}

# connected undirected edges for distance
sh_edges = [
    ["W", "X"],
    ["X", "Y"],
    ["Z", "Y"],
    ["Z", "V"],
    ["W", "V"]
]

# water and land grid
grid = [
    ['W', 'L', 'W', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W', 'W'],
    ['L', 'W', 'L', 'L', 'L', 'W'],
    ['W', 'L', 'W', 'W', 'L', 'W']
]
