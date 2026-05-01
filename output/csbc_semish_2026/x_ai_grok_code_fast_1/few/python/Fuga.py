import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
Xe = int(input_data[2])
Ye = int(input_data[3])
Xs = int(input_data[4])
Ys = int(input_data[5])

free = [[False] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i % 2 == 0 and j % 2 == 0:
            free[i][j] = False
        else:
            free[i][j] = True

visited = [[False] * (M + 1) for _ in range(N + 1)]
max_length = 0

def dfs(x, y, length):
    global max_length
    if x == Xs and y == Ys:
        max_length = max(max_length, length)
        return
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and free[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, length + 1)
    visited[x][y] = False

dfs(Xe, Ye, 1)
print(max_length)