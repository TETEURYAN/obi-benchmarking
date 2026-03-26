import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N)]
deg = [0] * N

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    deg[u] += 1
    deg[v] += 1

if N == 2:
    print(1)
    sys.exit()

dist = [-1] * N
q = deque()

for i in range(N):
    if deg[i] == 1:
        dist[i] = 0
        q.append(i)

ans = 10**18

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
        else:
            if dist[v] >= 0 and dist[v] != dist[u] - 1:
                cand = dist[u] + dist[v] + 1
                if cand < ans:
                    ans = cand

print(ans)