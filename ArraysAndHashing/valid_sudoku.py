"""
Don't be afraid to expend more memory when needed.
"""

def is_valid_sudoku(board: list):
    colmap = {}

    for i in range(9):
        colmap[i] = set()

    for r in range(9):
        hashset = set()

        for r_num in board[r]:
            if r_num == '.':
                continue

            if r_num in hashset:
                return False

            hashset.add(r_num)

        for c in range(9):
            c_num = board[r][c]

            if c_num == '.':
                continue

            if c_num in colmap[c]:
                return False

            colmap[c].add(c_num)

    return










