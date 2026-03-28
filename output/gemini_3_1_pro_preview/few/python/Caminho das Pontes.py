import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 2)]
idx = 2
for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    w = int(input_data[idx+2])
    adj[u].append((v, w))
    adj[v].append((u, w))
    idx += 3

dist = [float('inf')] * (n + 2)
dist[0] = 0

pq = [(0, 0)]

while pq:
    d, u = heapq.heappop(pq)
    
    if d > dist[u]:
        continue
        
    if u == n + 1:
        print(d)
        exit()
        
    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

print(dist[n + 1])