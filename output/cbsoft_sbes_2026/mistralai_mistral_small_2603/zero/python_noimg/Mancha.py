
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

    # Find all mancha pixels
    mancha = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '*':
                mancha.append((i, j))

    if len(mancha) < 2:
        print("N")
        return

    # Directions for BFS: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Check all pairs of mancha pixels
    for i in range(len(mancha)):
        for j in range(i+1, len(mancha)):
            P = mancha[i]
            Q = mancha[j]
            manhattan = abs(P[0] - Q[0]) + abs(P[1] - Q[1])

            # BFS to find shortest path in mancha
            visited = [[False]*N for _ in range(N)]
            queue = deque()
            queue.append((P[0], P[1], 0))
            visited[P[0]][P[1]] = True
            found = False

            while queue:
                x, y, dist = queue.popleft()
                if (x, y) == Q:
                    found = True
                    break
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '*':
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

            if not found:
                print("N")
                return

            if dist != manhattan:
                print("N")
                return

    print("S")

if __name__ == "__main__":
    main()
