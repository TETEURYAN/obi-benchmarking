import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    c = int(input_data[idx+2])
    adj[u].append((v, c))
    adj[v].append((u, c))
    idx += 3

dist = [float('inf')] * (n + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    
    if d > dist[u]:
        continue
        
    if u == n:
        print(d)
        exit()
        
    for v, c in adj[u]:
        if dist[u] + c < dist[v]:
            dist[v] = dist[u] + c
            heapq.heappush(pq, (dist[v], v))