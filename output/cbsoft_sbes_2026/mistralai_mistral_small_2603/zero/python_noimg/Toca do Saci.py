
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    grid = []
    start_i, start_j = -1, -1
    end_i, end_j = -1, -1

    for i in range(N):
        row = list(map(int, data[idx:idx+M]))
        idx += M
        grid.append(row)
        for j in range(M):
            if row[j] == 2:
                start_i, start_j = i, j
            elif row[j] == 3:
                end_i, end_j = i, j

    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((start_i, start_j, 0))
    visited[start_i][start_j] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j, steps = q.popleft()
        if i == end_i and j == end_j:
            print(steps)
            return

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and (grid[ni][nj] == 1 or grid[ni][nj] == 3):
                    visited[ni][nj] = True
                    q.append((ni, nj, steps + 1))

if __name__ == "__main__":
    main()
