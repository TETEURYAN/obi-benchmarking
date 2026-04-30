
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

if N == 0:
    print(0)
    sys.exit(0)

visited = [False] * (N + 1)
queue = deque()

queue.append((N, 0))
visited[N] = True

while queue:
    current, dist = queue.popleft()
    if current == 0:
        print(dist)
        sys.exit(0)
    
    s = str(current)
    digits = set()
    for c in s:
        d = int(c)
        if d > 0 and d not in digits:
            digits.add(d)
            nxt = current - d
            if nxt >= 0 and not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, dist + 1))
