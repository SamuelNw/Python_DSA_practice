"""
Return Number of Islands.
"""

from typing import List
from blueprint import grid


# DFS solution.
def count_islands(grid: List[list]) -> int:
    visited = set()
    count = 0
    ROWS, COLS = len(grid), len(grid[0])

    for r in range(ROWS):
        for c in range(COLS):
            if (explore(grid, r, c, visited)) == True:
                count += 1

    return count


def explore(grid: List[list], row: int, col: int, visited: set) -> bool:
    row_in_bounds = 0 <= row < len(grid)
    col_in_bounds = 0 <= col < len(grid[0])

    if not row_in_bounds or not col_in_bounds:
        return False

    if grid[row][col] == "W":
        return False

    pos = (row, col)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    explore(grid, row, col + 1, visited)
    explore(grid, row, col - 1, visited)

    return True


print(count_islands(grid))  # --> 5
