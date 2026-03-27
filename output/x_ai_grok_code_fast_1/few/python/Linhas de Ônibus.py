import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
T = int(input_data[idx])
idx += 1
L = int(input_data[idx])
idx += 1
O = int(input_data[idx])
idx += 1
D = int(input_data[idx])
idx += 1

lines = []
for i in range(L):
    C = int(input_data[idx])
    idx += 1
    terminals = [int(input_data[idx + j]) for j in range(C)]
    idx += C
    lines.append(set(terminals))

terminal_to_lines = [[] for _ in range(T + 1)]
for i in range(1, L + 1):
    for term in lines[i - 1]:
        terminal_to_lines[term].append(i)

adj = [[] for _ in range(L + 1)]
for term in range(1, T + 1):
    lst = terminal_to_lines[term]
    for j in range(len(lst)):
        for k in range(j + 1, len(lst)):
            a, b = lst[j], lst[k]
            adj[a].append(b)
            adj[b].append(a)

start_lines = terminal_to_lines[O]
dest_lines = terminal_to_lines[D]

dist = [-1] * (L + 1)
q = deque()
for sl in start_lines:
    dist[sl] = 0
    q.append(sl)

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

min_dist = float('inf')
for dl in dest_lines:
    if dist[dl] != -1:
        min_dist = min(min_dist, dist[dl])

print(min_dist + 1)