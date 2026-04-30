import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    C = int(input_data[1])
    K = int(input_data[2])
    
    grid = []
    idx = 3
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    dist = [[float('inf')] * C for _ in range(L)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while pq:
        d, r, c = heappop(pq)
        
        if d > dist[r][c]:
            continue
            
        if r == L - 1 and c == C - 1:
            print(d)
            return
            
        p_u = grid[r][c]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < L and 0 <= nc < C:
                p_v = grid[nr][nc]
                
                if p_u != -1:
                    if p_v == -1:
                        nd = d + 1
                        if nd < dist[nr][nc]:
                            dist[nr][nc] = nd
                            heappush(pq, (nd, nr, nc))
                    else:
                        if (p_u + 1) % K == p_v:
                            nd = d + 1
                            if nd < dist[nr][nc]:
                                dist[nr][nc] = nd
                                heappush(pq, (nd, nr, nc))
                else:
                    if p_v == -1:
                        nd = d + 1
                        if nd < dist[nr][nc]:
                            dist[nr][nc] = nd
                            heappush(pq, (nd, nr, nc))
                    else:
                        wait_time = (p_v - (d + 1)) % K
                        nd = d + 1 + wait_time
                        if nd < dist[nr][nc]:
                            dist[nr][nc] = nd
                            heappush(pq, (nd, nr, nc))
                            
    print(-1)

if __name__ == '__main__':
    solve()