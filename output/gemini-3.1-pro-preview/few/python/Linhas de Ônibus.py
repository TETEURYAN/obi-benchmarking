import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

T = int(input_data[0])
L = int(input_data[1])
O = int(input_data[2])
D = int(input_data[3])

terminals_of_line = [[] for _ in range(L + 1)]
lines_of_terminal = [[] for _ in range(T + 1)]

idx = 4
for i in range(1, L + 1):
    C = int(input_data[idx])
    idx += 1
    for _ in range(C):
        terminal = int(input_data[idx])
        terminals_of_line[i].append(terminal)
        lines_of_terminal[terminal].append(i)
        idx += 1

if O == D:
    print(0)
    exit()

visited_terminals = [False] * (T + 1)
visited_lines = [False] * (L + 1)
dist = [-1] * (T + 1)

q = deque()
q.append(O)
visited_terminals[O] = True
dist[O] = 0

while q:
    u = q.popleft()
    
    for l in lines_of_terminal[u]:
        if not visited_lines[l]:
            visited_lines[l] = True
            for v in terminals_of_line[l]:
                if not visited_terminals[v]:
                    visited_terminals[v] = True
                    dist[v] = dist[u] + 1
                    if v == D:
                        print(dist[v])
                        exit()
                    q.append(v)