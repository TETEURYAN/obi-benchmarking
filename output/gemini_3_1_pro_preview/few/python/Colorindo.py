import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

N = int(input_data[0])
M = int(input_data[1])
X = int(input_data[2])
Y = int(input_data[3])
K = int(input_data[4])

visited = [[False] * (M + 1) for _ in range(N + 1)]

idx = 5
for _ in range(K):
    A = int(input_data[idx])
    B = int(input_data[idx+1])
    if 1 <= A <= N and 1 <= B <= M:
        visited[A][B] = True
    idx += 2

queue = deque([(X, Y)])
visited[X][Y] = True
painted_count = 0

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

while queue:
    cx, cy = queue.popleft()
    painted_count += 1
    
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if 1 <= nx <= N and 1 <= ny <= M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

print(painted_count)