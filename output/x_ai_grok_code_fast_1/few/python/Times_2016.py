import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1

adj = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    M = int(input_data[idx])
    idx += 1
    for _ in range(M):
        X = int(input_data[idx])
        idx += 1
        adj[i].append(X)

color = [-1] * (N + 1)
color[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for v in adj[u]:
        if color[v] == -1:
            color[v] = 1 - color[u]
            q.append(v)

team1 = [i for i in range(1, N + 1) if color[i] == 0]
team2 = [i for i in range(1, N + 1) if color[i] == 1]

print(*sorted(team1))
print(*sorted(team2))