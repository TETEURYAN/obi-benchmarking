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
    p = int(input_data[idx])
    q = int(input_data[idx+1])
    d = int(input_data[idx+2])
    adj[p].append((q, d))
    adj[q].append((p, d))
    idx += 3

queue = deque([(a, 0)])
visited = [False] * (n + 1)
visited[a] = True

while queue:
    curr, dist = queue.popleft()
    
    if curr == b:
        print(dist)
        break
        
    for neighbor, weight in adj[curr]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append((neighbor, dist + weight))