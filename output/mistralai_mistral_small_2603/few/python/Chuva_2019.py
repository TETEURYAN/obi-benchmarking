
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2
    grid = []
    for _ in range(N):
        grid.append(list(data[idx]))
        idx += 1

    q = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'o':
                q.append((i, j))

    while q:
        i, j = q.popleft()
        if i + 1 < N and grid[i + 1][j] == '.' and (i + 1) % 2 == 1:
            grid[i + 1][j] = 'o'
            q.append((i + 1, j))
        if i - 1 >= 0 and grid[i - 1][j] == '.' and (i - 1) % 2 == 1:
            grid[i - 1][j] = 'o'
            q.append((i - 1, j))
        if j + 1 < M and grid[i][j + 1] == '.' and (i % 2 == 0 or (i % 2 == 1 and grid[i][j + 1] != '#')):
            if i % 2 == 0:
                grid[i][j + 1] = 'o'
                q.append((i, j + 1))
            else:
                if j + 1 < M and grid[i][j + 1] == '.' and (i + 1 < N and grid[i + 1][j + 1] == '#'):
                    grid[i][j + 1] = 'o'
                    q.append((i, j + 1))
        if j - 1 >= 0 and grid[i][j - 1] == '.' and (i % 2 == 0 or (i % 2 == 1 and grid[i][j - 1] != '#')):
            if i % 2 == 0:
                grid[i][j - 1] = 'o'
                q.append((i, j - 1))
            else:
                if j - 1 >= 0 and grid[i][j - 1] == '.' and (i + 1 < N and grid[i + 1][j - 1] == '#'):
                    grid[i][j - 1] = 'o'
                    q.append((i, j - 1))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
