"""
Given an m * n matrix with "L" for land and "W" for water inputs;
Return Number of Islands.
"""

from typing import List
from blueprint import grid
import collections


# RECURSIVE DFS Implementation:
def count_islands(grid: List[List[str]]) -> int:
    visited = set()
    count = 0
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(grid: List[List[str]], r: int, c: int, seen: set) -> bool:
        if (
            (r < 0 or c < 0) or
            (r >= ROWS or c >= COLS) or
            (grid[r][c] == "W") or
            ((r, c) in seen)
        ):
            return False

        seen.add((r, c))

        dfs(grid, r + 1, c, seen)
        dfs(grid, r - 1, c, seen)
        dfs(grid, r, c + 1, seen)
        dfs(grid, r, c - 1, seen)

        return True

    for r in range(ROWS):
        for c in range(COLS):
            if (dfs(grid, r, c, visited)) == True:
                count += 1

    return count


# BFS Implementation:
def count_islands_bfs(grid: List[List[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    seen = set()
    islands = 0

    def bfs(r: int, c: int) -> None:
        q = collections.deque()
        q.append((r, c))
        seen.add((r, c))
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, - 1]
        ]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    (r in range(ROWS)) and
                    (c in range(COLS)) and
                    (grid[r][c] == "L") and
                    ((r, c) not in seen)
                ):
                    q.append((r, c))
                    seen.add((r, c))

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "L" and not (row, col) in seen:
                bfs(row, col)
                islands += 1

    return islands


"""
COMPLEXITY ANALYSIS (for both algorithms):

Time Complexity -> O(n * m)
Space Complexity -> O(n * m)
"""


print(count_islands(grid))  # --> 5
print(count_islands_bfs(grid))  # --> 5
