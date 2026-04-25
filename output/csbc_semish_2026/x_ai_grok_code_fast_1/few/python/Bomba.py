import sys
from collections import deque

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx += 1
E = int(input_data[idx]); idx += 1
S = int(input_data[idx]); idx += 1
M = int(input_data[idx]); idx += 1
adj = [[] for _ in range(N)]
for _ in range(M):
    A = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    adj[A].append((B, T))
visited = [[False] * 3 for _ in range(N)]
q = deque()
q.append((E, 0, 0))
visited[E][0] = True
found = False
min_time = -1
while q:
    node, mod, time = q.popleft()
    if node == S:
        min_time = time
        found = True
        break
    for next_node, T in adj[node]:
        if (mod == 0 and T == 1) or (mod != 0 and T == 0):
            next_mod = (mod + 1) % 3
            next_time = time + 1
            if not visited[next_node][next_mod]:
                visited[next_node][next_mod] = True
                q.append((next_node, next_mod, next_time))
if found:
    print(min_time)
else:
    print('*')