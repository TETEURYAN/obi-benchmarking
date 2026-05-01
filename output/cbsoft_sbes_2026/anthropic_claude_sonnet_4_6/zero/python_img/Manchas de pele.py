import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    grid = []
    for i in range(N):
        row = [int(input_data[idx + j]) for j in range(M)]
        idx += M
        grid.append(row)
    
    visited = [[False] * M for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    
    print(count)

main()