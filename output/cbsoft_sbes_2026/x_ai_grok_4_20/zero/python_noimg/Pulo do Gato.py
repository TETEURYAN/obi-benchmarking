
import sys
from collections import deque

C = int(input())
tiles = list(map(int, input().split()))

if tiles[0] == 0 or tiles[-1] == 0:
    print(-1)
    sys.exit(0)

dist = [-1] * C
dist[0] = 0
q = deque([0])

while q:
    pos = q.popleft()
    if pos == C - 1:
        print(dist[pos])
        sys.exit(0)
    
    for jump in range(1, 3):
        nxt = pos + jump
        if nxt < C and tiles[nxt] == 1 and dist[nxt] == -1:
            dist[nxt] = dist[pos] + 1
            q.append(nxt)

print(-1)
