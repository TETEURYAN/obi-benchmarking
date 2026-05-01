from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    
    print(count)

main()