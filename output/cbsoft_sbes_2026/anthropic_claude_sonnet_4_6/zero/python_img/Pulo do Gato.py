from collections import deque

C = int(input())
tiles = list(map(int, input().split()))

dist = [-1] * C
dist[0] = 0
q = deque([0])

while q:
    pos = q.popleft()
    for jump in [1, 2]:
        npos = pos + jump
        if npos < C and tiles[npos] == 1 and dist[npos] == -1:
            dist[npos] = dist[pos] + 1
            q.append(npos)

print(dist[C-1])