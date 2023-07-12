from typing import List, Tuple


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(b: List[List[int]]) -> None:
    """Use backtracking to fill in all board positions."""
    find = find_empty_spot(b)
    if not find:
        return True
    else:
        row, col = find

    for choice in range(1, 10):
        if valid(b, (row, col), choice):
            b[row][col] = choice

            if solve(b):
                return True

            b[row][col] = 0

    return False


def valid(b: List[List[int]], pos: Tuple[int], num: int) -> bool:
    """Validate our choice as per the current - row, column, and 3 * 3 box."""

    # check row:
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    # check column:
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # check box:
    box_x = pos[1] // 3         # box on the x-axis
    box_y = pos[0] // 3         # box on the y-axis

    for i in range(box_y * 3, (box_y * 3) + 3):
        for j in range(box_x * 3, (box_x * 3) + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board: List[List[int]]) -> None:
    """Print the current state of the board."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(str(board[i][j]) + " | ")
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_spot(board: List[List[int]]) -> Tuple[int]:
    """Find the next empty spot on the board."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


print_board(board)
solve(board)
print(("\n" * 2) + "*****    SOLVED BOARD    *******" + ("\n" * 2))
print_board(board)
