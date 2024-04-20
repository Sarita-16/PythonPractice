def is_valid_sudoku(board):
    def is_valid_row(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        return True

    def is_valid_column(board):
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not is_valid_unit(column):
                return False
        return True

    def is_valid_box(board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                if not is_valid_unit(box):
                    return False
        return True

    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))

    return is_valid_row(board) and is_valid_column(board) and is_valid_box(board)


# Example usage:
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(is_valid_sudoku(board))  # Output: True
