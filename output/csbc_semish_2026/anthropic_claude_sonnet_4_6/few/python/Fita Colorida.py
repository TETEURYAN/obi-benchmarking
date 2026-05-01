import sys
from collections import deque

data = sys.stdin.read().split()
n = int(data[0])
tape = list(map(int, data[1:n+1]))

dist = [9] * n
q = deque()

for i in range(n):
    if tape[i] == 0:
        dist[i] = 0
        q.append(i)

while q:
    pos = q.popleft()
    for npos in (pos - 1, pos + 1):
        if 0 <= npos < n and dist[npos] == 9 and tape[npos] != 0:
            new_dist = dist[pos] + 1
            if new_dist < dist[npos]:
                dist[npos] = min(new_dist, 9)
                if dist[npos] < 9:
                    q.append(npos)

print(*dist)