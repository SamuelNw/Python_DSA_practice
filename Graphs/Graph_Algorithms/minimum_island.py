"""
Minimum island.
"""

from typing import List
from blueprint import grid


# DFS solution

def minimum_island(grid: List[list]) -> int:
    visited = set()
    smallest = float("inf")
    ROWS, COLS = len(grid), len(grid[0])

    for r in range(ROWS):
        for c in range(COLS):
            size = explore_size(grid, r, c, visited)
            if size > 0:
                smallest = min(smallest, size)

    return smallest


def explore_size(grid: List[list], row: int, col: int, visited: set) -> int:
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    if grid[row][col] == "W":
        return 0

    pos = (row, col)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1

    size += explore_size(grid, row - 1, col, visited)
    size += explore_size(grid, row + 1, col, visited)
    size += explore_size(grid, row, col + 1, visited)
    size += explore_size(grid, row, col + 1, visited)

    return size


print(minimum_island(grid))
