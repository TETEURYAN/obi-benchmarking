
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

L = int(data[0])
C = int(data[1])
K = int(data[2])

grid = []
index = 3
for i in range(L):
    row = []
    for j in range(C):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

INF = 10**18
dist = [[[INF] * K for _ in range(C)] for _ in range(L)]
dist[0][0][0] = 0

q = deque([(0, 0, 0)])

while q:
    r, c, t = q.popleft()
    d = dist[r][c][t]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < L and 0 <= nc < C:
            p = grid[nr][nc]
            nt = (t + 1) % K
            if p == -1:
                if dist[nr][nc][nt] > d + 1:
                    dist[nr][nc][nt] = d + 1
                    q.append((nr, nc, nt))
            else:
                if p == nt and dist[nr][nc][nt] > d + 1:
                    dist[nr][nc][nt] = d + 1
                    q.append((nr, nc, nt))
    
    p = grid[r][c]
    if p == -1:
        nt = (t + 1) % K
        if dist[r][c][nt] > d + 1:
            dist[r][c][nt] = d + 1
            q.append((r, c, nt))

ans = INF
for t in range(K):
    ans = min(ans, dist[L-1][C-1][t])

print(ans if ans < INF else -1)
