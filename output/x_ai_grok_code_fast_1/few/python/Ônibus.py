import sys
from collections import deque

input_data = sys.stdin.read().split()
N = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
adj = [[] for _ in range(N + 1)]
idx = 3
for _ in range(N - 1):
    P = int(input_data[idx])
    Q = int(input_data[idx + 1])
    adj[P].append(Q)
    adj[Q].append(P)
    idx += 2
dist = [-1] * (N + 1)
dist[A] = 0
q = deque([A])
while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
print(dist[B])