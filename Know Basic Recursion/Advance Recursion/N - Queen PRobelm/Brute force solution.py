def isSafe(row, col, board, n):
    dupRow = row
    dupCol = col

    # lower diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    # same col
    row = dupRow
    col = dupCol

    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    # upper diagonal

    row = dupRow
    col = dupCol
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1
    return True


def N_Queen(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return

    for row in range(n):
        if isSafe(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
            N_Queen(col + 1, board, ans, n)
            board[row] = board[row][:col] + '.' + board[row][col + 1:]


def printQueen(n):
    ans = []
    board = ['.' * n for _ in range(n)]
    N_Queen(0, board, ans, n)
    return ans


print(printQueen(4))
