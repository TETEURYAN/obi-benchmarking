import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

adj = [[] for _ in range(n + 1)]
idx = 1
for i in range(1, n + 1):
    m = int(input_data[idx])
    idx += 1
    for _ in range(m):
        v = int(input_data[idx])
        adj[i].append(v)
        idx += 1

color = [0] * (n + 1)

for i in range(1, n + 1):
    if color[i] == 0:
        color[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            nxt_c = 3 - color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = nxt_c
                    q.append(v)

team1 = []
team2 = []
for i in range(1, n + 1):
    if color[i] == 1:
        team1.append(i)
    else:
        team2.append(i)

print(*(team1))
print(*(team2))