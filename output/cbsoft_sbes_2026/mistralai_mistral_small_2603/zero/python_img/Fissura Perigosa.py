
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, f = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+n]]

    if grid[0][0] <= str(f):
        q = deque()
        q.append((0, 0))
        grid[0][0] = '*'

        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] != '*' and int(grid[ni][nj]) <= f:
                        grid[ni][nj] = '*'
                        q.append((ni, nj))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
