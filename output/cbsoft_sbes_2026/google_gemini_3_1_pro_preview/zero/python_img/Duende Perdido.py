
import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    grid = []
    idx = 2
    start_r = -1
    start_c = -1
    
    for i in range(N):
        row = []
        for j in range(M):
            val = int(input_data[idx])
            idx += 1
            row.append(val)
            if val == 3:
                start_r = i
                start_c = j
        grid.append(row)
        
    queue = deque([(start_r, start_c, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[start_r][start_c] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if grid[r][c] == 0:
            print(dist)
            return
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] != 2:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

if __name__ == '__main__':
    main()
