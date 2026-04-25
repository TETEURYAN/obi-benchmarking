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
    p = int(input_data[idx+2])
    adj[u].append((v, p))
    adj[v].append((u, p))
    idx += 3

s = int(input_data[idx])

dist = [float('inf')] * (n + 1)
dist[s] = 0

pq = [(0, s)]

while pq:
    d, u = heapq.heappop(pq)
    
    if d > dist[u]:
        continue
        
    for v, p in adj[u]:
        if d + p < dist[v]:
            dist[v] = d + p
            heapq.heappush(pq, (dist[v], v))

min_ping = float('inf')
max_ping = -1

for i in range(1, n + 1):
    if i != s:
        if dist[i] < min_ping:
            min_ping = dist[i]
        if dist[i] > max_ping:
            max_ping = dist[i]

print(max_ping - min_ping)