import sys
from collections import deque

N = int(sys.stdin.read().strip())
dist = [float('inf')] * (N + 1)
dist[N] = 0
q = deque([N])
while q:
    curr = q.popleft()
    if curr == 0:
        break
    s = str(curr)
    digits = set(s)
    for d in digits:
        if d == '0':
            continue
        next_n = curr - int(d)
        if next_n >= 0 and dist[next_n] == float('inf'):
            dist[next_n] = dist[curr] + 1
            q.append(next_n)
print(dist[0])