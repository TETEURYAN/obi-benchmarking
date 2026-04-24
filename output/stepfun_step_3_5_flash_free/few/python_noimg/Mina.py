import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        grid.append(row)
        idx += n

    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = 0
    dq = deque()
    dq.append((0, 0))
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while dq:
        x, y = dq.popleft()
        if x == n-1 and y == n-1:
            break
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                w = grid[nx][ny]
                nd = dist[x][y] + w
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    if w == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

    print(dist[n-1][n-1])

if __name__ == "__main__":
    main()