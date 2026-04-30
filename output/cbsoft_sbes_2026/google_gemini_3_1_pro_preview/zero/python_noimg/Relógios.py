import sys
from heapq import heappush, heappop

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    L = int(data[0])
    C = int(data[1])
    K = int(data[2])
    
    grid = []
    idx = 3
    for _ in range(L):
        row = []
        for _ in range(C):
            row.append(int(data[idx]))
            idx += 1
        grid.append(row)
        
    dist = [[float('inf')] * C for _ in range(L)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        d, r, c = heappop(pq)
        
        if d > dist[r][c]:
            continue
            
        if r == L - 1 and c == C - 1:
            print(d)
            return
            
        curr_P = grid[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < L and 0 <= nc < C:
                next_P = grid[nr][nc]
                
                if curr_P != -1:
                    if next_P == -1:
                        nd = d + 1
                    else:
                        if (curr_P + 1) % K == next_P:
                            nd = d + 1
                        else:
                            continue
                else:
                    if next_P == -1:
                        nd = d + 1
                    else:
                        nd = d + 1 + (next_P - (d + 1)) % K
                        
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heappush(pq, (nd, nr, nc))
                    
    print(-1)

if __name__ == '__main__':
    solve()