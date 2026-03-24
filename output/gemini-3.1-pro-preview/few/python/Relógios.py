import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])
K = int(input_data[2])

grid = []
idx = 3
for _ in range(L):
    row = []
    for _ in range(C):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)

dist = [[float('inf')] * C for _ in range(L)]
dist[0][0] = 0

pq = [(0, 0, 0)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while pq:
    t, r, c = heapq.heappop(pq)
    
    if t > dist[r][c]:
        continue
        
    if r == L - 1 and c == C - 1:
        print(t)
        exit()
        
    P = grid[r][c]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < L and 0 <= nc < C:
            nP = grid[nr][nc]
            
            if P == -1:
                if nP == -1:
                    nt = t + 1
                else:
                    wait_time = (nP - (t + 1)) % K
                    nt = t + 1 + wait_time
            else:
                if nP == -1:
                    nt = t + 1
                else:
                    if (t + 1) % K == nP:
                        nt = t + 1
                    else:
                        continue
                        
            if nt < dist[nr][nc]:
                dist[nr][nc] = nt
                heapq.heappush(pq, (nt, nr, nc))

print(-1)