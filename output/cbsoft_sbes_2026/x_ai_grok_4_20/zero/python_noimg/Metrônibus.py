
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index]); index += 1
K1 = int(data[index]); index += 1
K2 = int(data[index]); index += 1
P = int(data[index]); index += 1

metro = [[] for _ in range(N+1)]
bus = [[] for _ in range(N+1)]

for _ in range(K1):
    u = int(data[index]); index += 1
    v = int(data[index]); index += 1
    metro[u].append(v)
    metro[v].append(u)

for _ in range(K2):
    u = int(data[index]); index += 1
    v = int(data[index]); index += 1
    bus[u].append(v)
    bus[v].append(u)

A = int(data[index]); index += 1
B = int(data[index]); index += 1

if A == B:
    print(0)
    sys.exit(0)

INF = 10**18
dist = [[INF, INF] for _ in range(N+1)]
# 0: metro, 1: bus

q = deque()

if metro[A]:
    dist[A][0] = P
    q.append((A, 0))
if bus[A]:
    dist[A][1] = P
    q.append((A, 1))

while q:
    u, mode = q.popleft()
    d = dist[u][mode]
    
    if mode == 0:  # metro
        for v in metro[u]:
            if dist[v][0] > d:
                dist[v][0] = d
                q.appendleft((v, 0))
    else:  # bus
        for v in bus[u]:
            if dist[v][1] > d:
                dist[v][1] = d
                q.appendleft((v, 1))
    
    # switch system
    new_mode = 1 - mode
    new_d = d + P
    if new_mode == 0:
        for v in metro[u]:
            if dist[v][0] > new_d:
                dist[v][0] = new_d
                q.append((v, 0))
    else:
        for v in bus[u]:
            if dist[v][1] > new_d:
                dist[v][1] = new_d
                q.append((v, 1))

ans = min(dist[B][0], dist[B][1])
if ans == INF:
    print(-1)
else:
    print(ans)
