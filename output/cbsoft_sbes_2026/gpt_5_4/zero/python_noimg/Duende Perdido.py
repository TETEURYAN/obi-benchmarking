from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = []
    start = None

    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        for j, v in enumerate(row):
            if v == 3:
                start = (i, j)

    dist = [[-1] * m for _ in range(n)]
    q = deque([start])
    si, sj = start
    dist[si][sj] = 0

    while q:
        i, j = q.popleft()

        if grid[i][j] == 0:
            print(dist[i][j])
            return

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != 2 and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))

if __name__ == "__main__":
    main()