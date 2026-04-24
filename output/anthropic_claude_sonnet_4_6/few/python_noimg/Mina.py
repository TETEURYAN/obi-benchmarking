import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[idx])); idx += 1
        grid.append(row)
    
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    dq = deque()
    dq.append((0, 0))
    
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while dq:
        r, c = dq.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                cost = grid[nr][nc]
                nd = dist[r][c] + cost
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
    
    print(dist[n-1][n-1])

solve()