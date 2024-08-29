# Time Complexity: O( N^M) (n raised to m)
# Space Complexity: O(N)
def isSafe(node, color, col, graph, n):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


def solve(node, N, M, graph, color):
    if node == N:
        return True

    for i in range(1, M + 1):
        if isSafe(node, color, M, graph, N):
            color[node] = i

            if solve(node + 1, N, M, graph, color):
                return True
            color[node] = 0
    return False


def graphColoring(graph, M, N):
    color = [0] * N
    if solve(0, N, M, graph, color):
        return True
    return False


N = 4
m = 3
graph = [[0 for i in range(101)] for j in range(101)]
graph[0][1] = 1
graph[1][0] = 1
graph[1][2] = 1
graph[2][1] = 1
graph[2][3] = 1
graph[3][2] = 1
graph[3][0] = 1
graph[0][3] = 1
graph[0][2] = 1
graph[2][0] = 1

print(1 if graphColoring(graph, m, N) else 0)


