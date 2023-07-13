"""
Return the size of the largest island given an n * m matrix
with "L" for land and "W" for water.
"""

from blueprint import grid
from typing import List


# RECURSIVE DFS Implementation:

def largest_island(grid: List[List[str]]) -> int:
    visited, largest = set(), float("-inf")
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(grid: List[List[str]], r: int, c: int, seen: set) -> int:
        if (
            (r < 0 or c < 0) or
            (r >= ROWS or c >= COLS) or
            (grid[r][c] == "W") or
            ((r, c) in seen)
        ):
            return 0

        seen.add((r, c))

        size = 1

        size += dfs(grid, r + 1, c, seen)
        size += dfs(grid, r - 1, c, seen)
        size += dfs(grid, r, c + 1, seen)
        size += dfs(grid, r, c - 1, seen)

        return size

    for row in range(ROWS):
        for col in range(COLS):
            size = dfs(grid, row, col, visited)
            if size:
                largest = max(size, largest)

    return largest


"""
COMPLEXITY ANALYSIS:
Time Complexity -> O(n * m)
Space Complexity -> O(n * m)
"""


print(largest_island(grid))     # -> 5
