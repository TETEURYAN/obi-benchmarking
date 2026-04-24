import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
a = int(input_data[1])
b = int(input_data[2])

adj = [[] for _ in range(n + 1)]
idx = 3
for _ in range(n - 1):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

dist = [-1] * (n + 1)
dist[a] = 0
queue = deque([a])

while queue:
    curr = queue.popleft()
    if curr == b:
        print(dist[curr])
        break
    for neighbor in adj[curr]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[curr] + 1
            queue.append(neighbor)