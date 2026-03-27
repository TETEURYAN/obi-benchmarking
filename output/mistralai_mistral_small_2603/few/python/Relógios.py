
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    idx = 0
    L = int(data[idx])
    C = int(data[idx+1])
    K = int(data[idx+2])
    idx += 3

    grid = []
    for _ in range(L):
        row = list(map(int, data[idx:idx+C]))
        grid.append(row)
        idx += C

    if grid[0][0] != 0:
        print(-1)
        return

    visited = [[-1 for _ in range(C)] for _ in range(L)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j, time = q.popleft()

        if i == L - 1 and j == C - 1:
            print(time)
            return

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < L and 0 <= nj < C:
                if grid[ni][nj] == -1:
                    if visited[ni][nj] == -1:
                        visited[ni][nj] = time + 1
                        q.append((ni, nj, time + 1))
                else:
                    if (time + 1) % K == grid[ni][nj]:
                        if visited[ni][nj] == -1:
                            visited[ni][nj] = time + 1
                            q.append((ni, nj, time + 1))

    print(-1)

if __name__ == "__main__":
    main()
