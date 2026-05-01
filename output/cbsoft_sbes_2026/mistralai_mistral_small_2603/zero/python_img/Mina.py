
import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    grid = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = grid[0][0]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + grid[nx][ny]
                    q.append((nx, ny))
                elif visited[nx][ny] > visited[x][y] + grid[nx][ny]:
                    visited[nx][ny] = visited[x][y] + grid[nx][ny]
                    q.append((nx, ny))

    print(visited[N-1][N-1])

if __name__ == "__main__":
    main()
