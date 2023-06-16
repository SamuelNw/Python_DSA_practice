# Undirected graph represented as an adjacency dictionary
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6],
    4: [1, 7, 8],
    5: [2, 9],
    6: [3, 10],
    7: [4, 11],
    8: [4, 12],
    9: [5, 13],
    10: [6, 14],
    11: [7, 15],
    12: [8],
    13: [9],
    14: [10],
    15: [11]
}


# Directed graph represented as an adjacency dictionary
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [2, 6],
    4: [6],
    5: [4, 6],
    6: [1]
}
