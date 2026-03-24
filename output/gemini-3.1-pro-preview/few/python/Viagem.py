import sys
from heapq import heappush, heappop

input_data = sys.stdin.read().split()
if not input_data:
    exit()

V = int(input_data[0])
N = int(input_data[1])
M = int(input_data[2])

adj = [[] for _ in range(N + 1)]
idx = 3
for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    t = int(input_data[idx+2])
    p = int(input_data[idx+3])
    adj[u].append((v, t, p))
    adj[v].append((u, t, p))
    idx += 4

X = int(input_data[idx])
Y = int(input_data[idx+1])

V_plus_1 = V + 1
best_time = [float('inf')] * ((N + 1) * V_plus_1)
best_time[X * V_plus_1] = 0

min_cost = [V_plus_1] * (N + 1)

pq = [(0, 0, X)]

while pq:
    t, c, u = heappop(pq)
    
    if t > best_time[u * V_plus_1 + c]:
        continue
        
    if u == Y:
        print(t)
        exit()
        
    if c >= min_cost[u]:
        continue
        
    min_cost[u] = c
    
    for v, edge_t, edge_p in adj[u]:
        nc = c + edge_p
        if nc <= V:
            nt = t + edge_t
            idx_v_nc = v * V_plus_1 + nc
            if nt < best_time[idx_v_nc]:
                best_time[idx_v_nc] = nt
                heappush(pq, (nt, nc, v))

print(-1)