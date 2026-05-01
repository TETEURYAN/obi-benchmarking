
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("N")
        return
    N = int(data[0])
    grid = []
    for i in range(1, N+1):
        grid.append(data[i].strip())

    # Find all '*' positions
    points = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '*':
                points.append((i, j))

    if len(points) < 2:
        print("S")
        return

    # Directions for BFS: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check all pairs of points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            start = points[i]
            end = points[j]
            # BFS to find shortest path in the mancha
            visited = [[False]*N for _ in range(N)]
            queue = deque()
            queue.append((start[0], start[1], 0))
            visited[start[0]][start[1]] = True
            found = False
            while queue:
                x, y, dist = queue.popleft()
                if (x, y) == end:
                    found = True
                    break
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and grid[nx][ny] == '*':
                            visited[nx][ny] = True
                            queue.append((nx, ny, dist + 1))
            if not found:
                print("N")
                return

            manhattan = abs(start[0] - end[0]) + abs(start[1] - end[1])
            if dist != manhattan:
                print("N")
                return

    print("S")

if __name__ == "__main__":
    main()
