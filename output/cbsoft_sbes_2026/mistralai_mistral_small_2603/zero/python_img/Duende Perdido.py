
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    start_i, start_j = -1, -1
    for i in range(n):
        row = list(map(int, data[2 + i * m : 2 + (i + 1) * m]))
        grid.append(row)
        for j in range(m):
            if row[j] == 3:
                start_i, start_j = i, j

    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((start_i, start_j, 0))
    visited[start_i][start_j] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j, dist = q.popleft()
        if grid[i][j] == 0:
            print(dist)
            return
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and grid[ni][nj] != 2:
                    visited[ni][nj] = True
                    q.append((ni, nj, dist + 1))

if __name__ == "__main__":
    main()
