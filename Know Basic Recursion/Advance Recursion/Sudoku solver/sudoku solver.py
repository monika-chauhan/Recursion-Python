# Three coditions we have to keep in mind
# 1.No repeating no in row (1-9)
# 2. No repeating no in col (1-9)
# 3. No repeating no in (3X3) matrix(1-9)

def isValid(row, col, board, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True


def sudoku(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for c in range(1, 10):
                    if isValid(i, j, board, c):
                        board[i][j] = c
                        if sudoku(board):
                            return True
                        else:
                            board[i][j] = "."
                return False
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sudoku(board))
