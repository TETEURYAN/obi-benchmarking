import sys
from collections import deque

input = sys.stdin.read
data = input().split()

idx = 0
N = int(data[idx]); idx += 1
M = int(data[idx]); idx += 1

adjC = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    adjC[a].append(b)
    adjC[b].append(a)

adjQ = [[] for _ in range(M + 1)]
for _ in range(M - 1):
    x = int(data[idx]); idx += 1
    y = int(data[idx]); idx += 1
    adjQ[x].append(y)
    adjQ[y].append(x)

def find_centers(adj, n):
    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        farthest = start
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[farthest]:
                        farthest = v
        return farthest, dist

    end1, _ = bfs(1)
    end2, dist_from_end1 = bfs(end1)

    path = []
    current = end2
    while current != end1:
        path.append(current)
        for v in adj[current]:
            if dist_from_end1[v] == dist_from_end1[current] - 1:
                current = v
                break
    path.append(end1)
    path.reverse()

    diam = len(path) - 1
    mid = diam // 2
    centers = [path[mid]]
    if diam % 2 == 1:
        centers.append(path[mid + 1])
    return centers

centers_C = find_centers(adjC, N)
centers_Q = find_centers(adjQ, M)

print(centers_C[0], centers_Q[0])