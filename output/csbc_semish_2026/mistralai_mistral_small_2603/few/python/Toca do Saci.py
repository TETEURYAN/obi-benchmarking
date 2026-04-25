
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    grid = []
    idx = 2
    start_i, start_j = -1, -1
    end_i, end_j = -1, -1

    for i in range(n):
        row = list(map(int, data[idx:idx + m]))
        grid.append(row)
        for j in range(m):
            if row[j] == 2:
                start_i, start_j = i, j
            elif row[j] == 3:
                end_i, end_j = i, j
        idx += m

    visited = [[False for _ in range(m)] for _ in range(n)]
    from collections import deque
    q = deque()
    q.append((start_i, start_j, 0))
    visited[start_i][start_j] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j, dist = q.popleft()
        if i == end_i and j == end_j:
            print(dist)
            return

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and grid[ni][nj] != 0:
                    visited[ni][nj] = True
                    q.append((ni, nj, dist + 1))

if __name__ == "__main__":
    main()
