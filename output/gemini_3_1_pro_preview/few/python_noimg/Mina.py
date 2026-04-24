import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
grid = []
idx = 1
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0

dq = deque([(0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while dq:
    r, c = dq.popleft()
    
    if r == N - 1 and c == N - 1:
        print(dist[r][c])
        break
        
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            cost = grid[nr][nc]
            if dist[r][c] + cost < dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + cost
                if cost == 0:
                    dq.appendleft((nr, nc))
                else:
                    dq.append((nr, nc))