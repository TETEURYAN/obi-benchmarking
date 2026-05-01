
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, F = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+N]]

    if grid[0][0] <= str(F):
        q = deque()
        q.append((0, 0))
        grid[0][0] = '*'

        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if grid[ni][nj] != '*' and int(grid[ni][nj]) <= F:
                        grid[ni][nj] = '*'
                        q.append((ni, nj))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
