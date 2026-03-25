import sys
from collections import deque

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

idx = 0
N = data[idx]
M = data[idx + 1]
idx += 2

P = data[idx]
idx += 1

stones = set()
for _ in range(P):
    c = data[idx]
    l = data[idx + 1]
    stones.add((c, l))
    idx += 2

start = (data[idx], data[idx + 1])
idx += 2
target = (data[idx], data[idx + 1])

q = deque([start])
visited = {start}
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

while q:
    c, l = q.popleft()
    if (c, l) == target:
        print('S')
        sys.exit()
    for dc, dl in dirs:
        for d in (1, 2, 3):
            nc = c + dc * d
            nl = l + dl * d
            nxt = (nc, nl)
            if nxt in stones and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

print('N')