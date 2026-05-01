
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])
    Xe = int(data[2])
    Ye = int(data[3])
    Xs = int(data[4])
    Ys = int(data[5])

    grid = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(2, N + 1, 2):
        for j in range(2, M + 1, 2):
            grid[i][j] = 1

    max_dist = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs():
        visited = [[-1] * (M + 1) for _ in range(N + 1)]
        q = deque()
        q.append((Xe, Ye))
        visited[Xe][Ye] = 1
        while q:
            x, y = q.popleft()
            if x == Xs and y == Ys:
                return visited[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx <= N and 1 <= ny <= M:
                    if visited[nx][ny] == -1:
                        if grid[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
                        else:
                            if nx + dx <= N and ny + dy <= M and grid[nx + dx][ny + dy] == 0 and visited[nx + dx][ny + dy] == -1:
                                visited[nx + dx][ny + dy] = visited[x][y] + 2
                                q.append((nx + dx, ny + dy))
        return -1

    for i in range(2, N + 1, 2):
        for j in range(2, M + 1, 2):
            for dx, dy in directions:
                ni1, nj1 = i + dx, j + dy
                ni2, nj2 = i + 2 * dx, j + 2 * dy
                if 1 <= ni1 <= N and 1 <= nj1 <= M and 1 <= ni2 <= N and 1 <= nj2 <= M:
                    if grid[ni1][nj1] == 0 and grid[ni2][nj2] == 0:
                        grid[i][j] = 0
                        grid[ni1][nj1] = 1
                        grid[ni2][nj2] = 1
                        current_dist = bfs()
                        if current_dist > max_dist:
                            max_dist = current_dist
                        grid[i][j] = 1
                        grid[ni1][nj1] = 0
                        grid[ni2][nj2] = 0
    print(max_dist)

if __name__ == "__main__":
    main()
