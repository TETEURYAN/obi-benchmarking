
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
L = int(data[index])
index += 1
O = int(data[index])
index += 1
D = int(data[index])
index += 1

lines = []
term_to_lines = [[] for _ in range(T + 1)]

for l in range(1, L + 1):
    C = int(data[index])
    index += 1
    terminals = []
    for _ in range(C):
        t = int(data[index])
        index += 1
        terminals.append(t)
        term_to_lines[t].append(l)
    lines.append(terminals)

if O == D:
    print(0)
    sys.exit(0)

graph = [[] for _ in range(L + 1)]
for t in range(1, T + 1):
    line_list = term_to_lines[t]
    for i in range(len(line_list)):
        for j in range(i + 1, len(line_list)):
            a = line_list[i]
            b = line_list[j]
            graph[a].append(b)
            graph[b].append(a)

queue = deque()
dist = [-1] * (L + 1)

for start_line in term_to_lines[O]:
    queue.append(start_line)
    dist[start_line] = 1

found = False
ans = -1
while queue:
    curr = queue.popleft()
    if curr in term_to_lines[D]:
        ans = dist[curr]
        found = True
        break
    for neigh in graph[curr]:
        if dist[neigh] == -1:
            dist[neigh] = dist[curr] + 1
            queue.append(neigh)

print(ans)
