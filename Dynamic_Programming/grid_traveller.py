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


# OR:
def grid_traveller_2(m, n):
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]


# returns fast
print(grid_traveller(250, 350))
print(grid_traveller_2(250, 350))
