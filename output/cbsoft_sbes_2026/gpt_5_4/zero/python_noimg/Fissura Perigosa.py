import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, f = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    if grid[0][0] > str(f):
        for row in grid:
            print(''.join(row))
        return

    q = deque()
    q.append((0, 0))
    grid[0][0] = '*'

    while q:
        i, j = q.popleft()

        if i > 0 and grid[i - 1][j] != '*' and grid[i - 1][j] <= str(f):
            grid[i - 1][j] = '*'
            q.append((i - 1, j))
        if i + 1 < n and grid[i + 1][j] != '*' and grid[i + 1][j] <= str(f):
            grid[i + 1][j] = '*'
            q.append((i + 1, j))
        if j > 0 and grid[i][j - 1] != '*' and grid[i][j - 1] <= str(f):
            grid[i][j - 1] = '*'
            q.append((i, j - 1))
        if j + 1 < n and grid[i][j + 1] != '*' and grid[i][j + 1] <= str(f):
            grid[i][j + 1] = '*'
            q.append((i, j + 1))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
