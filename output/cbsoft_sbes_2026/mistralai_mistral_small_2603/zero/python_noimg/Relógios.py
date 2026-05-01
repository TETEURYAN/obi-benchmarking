
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
    
    start = (0, 0)
    end = (L-1, C-1)
    
    if grid[0][0] != 0:
        print(-1)
        return
    
    visited = [[-1 for _ in range(C)] for _ in range(L)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x, y, time = q.popleft()
        
        if (x, y) == end:
            print(time)
            return
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < L and 0 <= ny < C:
                if grid[nx][ny] == -1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = time + 1
                        q.append((nx, ny, time + 1))
                else:
                    if (time + 1) % K == grid[nx][ny]:
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = time + 1
                            q.append((nx, ny, time + 1))
        
        if visited[x][y] == time:
            for t in range(1, K + 1):
                new_time = time + t
                if new_time % K == grid[x][y]:
                    if visited[x][y] == -1 or new_time < visited[x][y]:
                        visited[x][y] = new_time
                        q.append((x, y, new_time))
    
    print(-1)

if __name__ == "__main__":
    main()
