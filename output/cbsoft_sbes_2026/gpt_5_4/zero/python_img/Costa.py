import sys
from collections import deque

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    grid = [input().strip() for _ in range(M)]

    visited = [[False] * (N + 2) for _ in range(M + 2)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    coast = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < M + 2 and 0 <= ny < N + 2):
                continue
            if 1 <= nx <= M and 1 <= ny <= N:
                if grid[nx - 1][ny - 1] == '#':
                    coast += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            else:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    print(coast)

if __name__ == "__main__":
    main()
