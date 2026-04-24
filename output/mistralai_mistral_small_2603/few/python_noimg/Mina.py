
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        grid.append(row)
        index += n

    if n == 1:
        print(0)
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        x, y, cost = queue.popleft()

        if x == n-1 and y == n-1:
            print(cost)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 1:
                    queue.append((nx, ny, cost + 1))
                else:
                    queue.appendleft((nx, ny, cost))

    print(-1)

if __name__ == "__main__":
    main()
