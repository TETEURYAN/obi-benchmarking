import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, F = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    if grid[0][0] > str(F):
        print('\n'.join(''.join(row) for row in grid))
        return

    q = deque()
    q.append((0, 0))
    grid[0][0] = '*'

    while q:
        i, j = q.popleft()

        if i > 0 and grid[i - 1][j] != '*' and grid[i - 1][j] <= str(F):
            grid[i - 1][j] = '*'
            q.append((i - 1, j))
        if i + 1 < N and grid[i + 1][j] != '*' and grid[i + 1][j] <= str(F):
            grid[i + 1][j] = '*'
            q.append((i + 1, j))
        if j > 0 and grid[i][j - 1] != '*' and grid[i][j - 1] <= str(F):
            grid[i][j - 1] = '*'
            q.append((i, j - 1))
        if j + 1 < N and grid[i][j + 1] != '*' and grid[i][j + 1] <= str(F):
            grid[i][j + 1] = '*'
            q.append((i, j + 1))

    print('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    main()