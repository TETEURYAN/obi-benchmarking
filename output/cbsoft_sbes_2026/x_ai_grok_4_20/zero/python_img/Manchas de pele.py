
import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    grid = []
    index = 2
    for i in range(N):
        row = [int(data[index + j]) for j in range(M)]
        grid.append(row)
        index += M
    
    if N == 0 or M == 0:
        print(0)
        return
    
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()
