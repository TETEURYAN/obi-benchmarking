import heapq
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    grid = []
    idx = 1
    for i in range(n):
        grid.append([int(x) for x in input_data[idx:idx+n]])
        idx += n
        
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        
        if d > dist[r][c]:
            continue
        if r == n - 1 and c == n - 1:
            print(d)
            return
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                weight = grid[nr][nc]
                if dist[nr][nc] > d + weight:
                    dist[nr][nc] = d + weight
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

solve()