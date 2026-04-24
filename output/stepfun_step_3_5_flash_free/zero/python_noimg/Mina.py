
import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = []
    for _ in range(n):
        row = [int(next(it)) for _ in range(n)]
        grid.append(row)
    
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    dq = deque([(0, 0)])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while dq:
        i, j = dq.popleft()
        d = dist[i][j]
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                w = grid[ni][nj]
                nd = d + w
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    if w == 0:
                        dq.appendleft((ni, nj))
                    else:
                        dq.append((ni, nj))
    
    print(dist[n-1][n-1])

if __name__ == "__main__":
    main()
