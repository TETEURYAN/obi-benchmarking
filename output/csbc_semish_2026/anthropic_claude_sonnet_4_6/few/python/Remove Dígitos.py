import sys
from collections import deque

def solve():
    N = int(sys.stdin.read().strip())
    
    dist = [-1] * (N + 1)
    dist[N] = 0
    queue = deque([N])
    
    while queue:
        cur = queue.popleft()
        if cur == 0:
            print(dist[0])
            return
        for ch in str(cur):
            d = int(ch)
            if d == 0:
                continue
            nxt = cur - d
            if nxt >= 0 and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    
    print(dist[0])

solve()