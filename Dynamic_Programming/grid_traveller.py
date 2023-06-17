"""
Return the distinct number of ways to travel through an m * n  grid.
"""


def grid_traveller(m: int, n: int, memo={}) -> int:
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    memo[(m, n)] = grid_traveller(m - 1, n, memo) + \
        grid_traveller(m, n - 1, memo)
    return memo[(m, n)]


# returns fast
print(grid_traveller(250, 350))
