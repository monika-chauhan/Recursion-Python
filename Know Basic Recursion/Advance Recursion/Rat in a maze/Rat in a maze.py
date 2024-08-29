# Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.
# Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).



def solve(i: int, j: int, a, n: int, ans, move: str, vis,di, dj):
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return
    dir = "DLRU"
    for ind in range(4):
        nexti = i + di[ind]
        nextj = j + dj[ind]
        if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
            vis[i][j] = 1
            solve(nexti, nextj, a, n, ans,move + dir[ind], vis, di, dj)
            vis[i][j] = 0


def findPath(m, n):
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [+1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    if m[0][0] == 1:
        solve(0, 0, m, n, ans, "", vis, di, dj)
    return ans


n = 4
m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(findPath(m,n))
