import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
adj = [[] for _ in range(n + 1)]

idx = 1
for i in range(1, n + 1):
    m = data[idx]
    idx += 1
    for _ in range(m):
        x = data[idx]
        idx += 1
        adj[i].append(x)

color = [-1] * (n + 1)
color[1] = 0
q = deque([1])

while q:
    u = q.popleft()
    cu = color[u]
    for v in adj[u]:
        if color[v] == -1:
            color[v] = cu ^ 1
            q.append(v)

for i in range(1, n + 1):
    if color[i] == -1:
        color[i] = 0
        q.append(i)
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)

team1 = []
team2 = []
for i in range(1, n + 1):
    if color[i] == 0:
        team1.append(str(i))
    else:
        team2.append(str(i))

sys.stdout.write(" ".join(team1) + "\n" + " ".join(team2) + "\n")