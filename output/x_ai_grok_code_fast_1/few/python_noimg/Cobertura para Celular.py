import sys
sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
N = int(input_data[0])
torres = []
idx = 1
for i in range(N):
    x = int(input_data[idx])
    y = int(input_data[idx + 1])
    torres.append((x, y))
    idx += 2
A = int(input_data[idx])
A2 = A * A

visited = [False] * N

def dfs(u):
    visited[u] = True
    for v in range(N):
        if not visited[v]:
            dx = torres[u][0] - torres[v][0]
            dy = torres[u][1] - torres[v][1]
            if dx * dx + dy * dy <= A2:
                dfs(v)

dfs(0)
if all(visited):
    print('S')
else:
    print('N')