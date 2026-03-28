import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
P = int(input_data[idx])
idx += 1
pedras = []
for _ in range(P):
    c = int(input_data[idx])
    l = int(input_data[idx + 1])
    pedras.append((c, l))
    idx += 2
Sc = int(input_data[idx])
SL = int(input_data[idx + 1])
idx += 2
Rc = int(input_data[idx])
RL = int(input_data[idx + 1])

# Encontrar índices de start e end
start = -1
end = -1
for i in range(P):
    if pedras[i] == (Sc, SL):
        start = i
    if pedras[i] == (Rc, RL):
        end = i

# Construir grafo
adj = [[] for _ in range(P)]
for i in range(P):
    for j in range(i + 1, P):
        c1, l1 = pedras[i]
        c2, l2 = pedras[j]
        if (c1 == c2 and abs(l1 - l2) <= 3) or (l1 == l2 and abs(c1 - c2) <= 3):
            adj[i].append(j)
            adj[j].append(i)

# BFS para verificar conectividade
from collections import deque
visited = [False] * P
queue = deque([start])
visited[start] = True
found = False
while queue:
    u = queue.popleft()
    if u == end:
        found = True
        break
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)

print('S' if found else 'N')