import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

if n == 2:
    print(1)
    exit()

adj = [[] for _ in range(n + 1)]
idx = 1
for _ in range(n - 1):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

dist = [-1] * (n + 1)
source = [-1] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if len(adj[i]) == 1:
        dist[i] = 0
        source[i] = i
        q.append(i)

min_dist = float('inf')

while q:
    u = q.popleft()
    
    if dist[u] * 2 >= min_dist:
        continue
        
    for v in adj[u]:
        if source[v] == -1:
            source[v] = source[u]
            dist[v] = dist[u] + 1
            q.append(v)
        elif source[v] != source[u]:
            current_dist = dist[u] + dist[v] + 1
            if current_dist < min_dist:
                min_dist = current_dist

print(min_dist)