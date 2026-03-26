
import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    grid = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        idx += N
        grid.append(row)
    
    # BFS com deque (0-1 BFS)
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0 if grid[0][0] == 0 else 1
    
    dq = deque()
    dq.append((0, 0))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = 1 if grid[nx][ny] == 1 else 0
                new_dist = dist[x][y] + cost
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    if cost == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
    
    print(dist[N-1][N-1])

if __name__ == "__main__":
    main()
