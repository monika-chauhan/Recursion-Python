def N_Queen(col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
    if col == n:
        ans.append(list(board))
        return
    for row in range(n):
        if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
            board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
            leftRow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[n - 1 + col - row] = 1
            N_Queen(col + 1, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
            board[row] = board[row][:col] + '.' + board[row][col + 1:]
            leftRow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[n - 1 + col - row] = 0


def printQueen(n):
    ans = []
    board = ['.' * n for _ in range(n)]
    lowerDiagonal = [0] * (2 * n - 1)
    upperDiagonal = [0] * (2 * n - 1)
    leftRow = [0] * n
    N_Queen(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
    return ans


print(printQueen(4))
