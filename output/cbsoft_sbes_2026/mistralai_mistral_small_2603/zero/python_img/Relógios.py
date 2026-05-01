
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    L = int(data[0])
    C = int(data[1])
    K = int(data[2])
    grid = []
    index = 3
    for i in range(L):
        row = list(map(int, data[index:index+C]))
        grid.append(row)
        index += C

    start_time = 0
    start_x, start_y = 0, 0
    end_x, end_y = L-1, C-1

    if grid[start_x][start_y] != 0:
        print(-1)
        return

    visited = [[-1 for _ in range(C)] for _ in range(L)]
    q = deque()
    q.append((start_x, start_y, start_time))
    visited[start_x][start_y] = start_time

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, t = q.popleft()

        if x == end_x and y == end_y:
            print(t)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < L and 0 <= ny < C:
                if grid[nx][ny] == -1:
                    if visited[nx][ny] == -1 or t + 1 < visited[nx][ny]:
                        visited[nx][ny] = t + 1
                        q.append((nx, ny, t + 1))
                else:
                    if (t + 1) % K == grid[nx][ny]:
                        if visited[nx][ny] == -1 or t + 1 < visited[nx][ny]:
                            visited[nx][ny] = t + 1
                            q.append((nx, ny, t + 1))

    print(-1)

if __name__ == "__main__":
    main()
