
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, M = map(int, data[0].split())
    grid = [list(line.strip()) for line in data[1:1+N]]

    q = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'o':
                q.append((i, j))
                break
        if q:
            break

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if grid[ni][nj] == '.':
                    if di == -1:
                        grid[ni][nj] = 'o'
                        q.append((ni, nj))
                    elif di == 0:
                        if dj == -1:
                            if (nj - 1 >= 0 and grid[ni][nj - 1] == 'o' and
                                ni + 1 < N and grid[ni + 1][nj - 1] == '#'):
                                grid[ni][nj] = 'o'
                                q.append((ni, nj))
                        elif dj == 1:
                            if (nj + 1 < M and grid[ni][nj + 1] == 'o' and
                                ni + 1 < N and grid[ni + 1][nj + 1] == '#'):
                                grid[ni][nj] = 'o'
                                q.append((ni, nj))
                    elif di == 1:
                        if grid[ni][nj] == '.':
                            grid[ni][nj] = 'o'
                            q.append((ni, nj))

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
