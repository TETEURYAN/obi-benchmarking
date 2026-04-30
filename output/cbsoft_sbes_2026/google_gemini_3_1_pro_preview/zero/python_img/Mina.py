import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    grid = []
    idx = 1
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    
    q = deque([(0, 0)])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c = q.popleft()
        
        if r == N - 1 and c == N - 1:
            print(dist[r][c])
            return
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                weight = grid[nr][nc]
                if dist[r][c] + weight < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + weight
                    if weight == 0:
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))

if __name__ == '__main__':
    solve()