import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
D = int(input_data[idx])
idx += 1
trees = []
for i in range(N):
    x = int(input_data[idx])
    y = int(input_data[idx + 1])
    trees.append((x, y))
    idx += 2

# Build graph
graph = [[] for _ in range(N)]
D2 = D * D
for i in range(N):
    for j in range(i + 1, N):
        dx = trees[i][0] - trees[j][0]
        dy = trees[i][1] - trees[j][1]
        if dx * dx + dy * dy <= D2:
            graph[i].append(j)
            graph[j].append(i)

# BFS to check connectivity
visited = [False] * N
queue = deque([0])
visited[0] = True
count = 1
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            count += 1
            queue.append(v)

if count == N:
    print('S')
else:
    print('N')