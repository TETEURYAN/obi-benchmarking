
import heapq

def solve():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    while pq:
        cost, r, c = heapq.heappop(pq)
        
        if cost > dist[r][c]:
            continue
        
        if r == n-1 and c == n-1:
            print(cost)
            return
        
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n:
                new_cost = cost + grid[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    
    print(dist[n-1][n-1])

solve()
