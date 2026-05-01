import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

T, L, O, D = data[0], data[1], data[2], data[3]

lines = [[] for _ in range(L)]
terminal_to_lines = [[] for _ in range(T + 1)]

idx = 4
start_lines = []
target_lines = []

for i in range(L):
    c = data[idx]
    idx += 1
    stops = data[idx:idx + c]
    idx += c
    lines[i] = stops
    has_o = False
    has_d = False
    for s in stops:
        terminal_to_lines[s].append(i)
        if s == O:
            has_o = True
        if s == D:
            has_d = True
    if has_o:
        start_lines.append(i)
    if has_d:
        target_lines.append(i)

target = [False] * L
for x in target_lines:
    target[x] = True

dist = [-1] * L
q = deque()

for x in start_lines:
    dist[x] = 1
    q.append(x)

used_terminal = [False] * (T + 1)

while q:
    line = q.popleft()
    if target[line]:
        print(dist[line])
        break
    for terminal in lines[line]:
        if used_terminal[terminal]:
            continue
        used_terminal[terminal] = True
        for nxt in terminal_to_lines[terminal]:
            if dist[nxt] == -1:
                dist[nxt] = dist[line] + 1
                q.append(nxt)