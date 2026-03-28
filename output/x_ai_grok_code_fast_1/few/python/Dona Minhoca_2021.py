import sys

data = sys.stdin.read().split()
N = int(data[0])
adj = [[] for _ in range(N + 1)]
idx = 1
for i in range(N - 1):
    x = int(data[idx])
    y = int(data[idx + 1])
    adj[x].append(y)
    adj[y].append(x)
    idx += 2

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = [start]
    far = start
    for u in q:
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                far = v
    return dist, far

dist1, A = bfs(1)
distA, B = bfs(A)
Diam = distA[B]
distB, _ = bfs(B)

lenS = sum(1 for d in distA[1:] if d == Diam)
lenT = sum(1 for d in distB[1:] if d == Diam)

print(Diam + 1)
print(lenS * lenT)