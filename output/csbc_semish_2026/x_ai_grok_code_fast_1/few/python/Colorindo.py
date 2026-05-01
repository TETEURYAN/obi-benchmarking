import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
X = int(input_data[idx])
idx += 1
Y = int(input_data[idx])
idx += 1
K = int(input_data[idx])
idx += 1

grid = [[0] * M for _ in range(N)]
for _ in range(K):
    A = int(input_data[idx])
    idx += 1
    B = int(input_data[idx])
    idx += 1
    grid[A-1][B-1] = 1

visited = [[False] * M for _ in range(N)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

queue = deque()
queue.append((X-1, Y-1))
visited[X-1][Y-1] = True
count = 1

while queue:
    i, j = queue.popleft()
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] == 0:
            visited[ni][nj] = True
            queue.append((ni, nj))
            count += 1

print(count)