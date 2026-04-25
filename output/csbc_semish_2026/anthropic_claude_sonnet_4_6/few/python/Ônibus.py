import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx+=1
A = int(input_data[idx]); idx+=1
B = int(input_data[idx]); idx+=1

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    p = int(input_data[idx]); idx+=1
    q = int(input_data[idx]); idx+=1
    adj[p].append(q)
    adj[q].append(p)

dist = [-1]*(N+1)
dist[A] = 0
queue = deque([A])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u]+1
            queue.append(v)

print(dist[B])