
import sys
sys.setrecursionlimit(400000)

from collections import deque

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

N, M = read_ints()

circle = [[] for _ in range(N+1)]
square = [[] for _ in range(M+1)]

for _ in range(N-1):
    a, b = read_ints()
    circle[a].append(b)
    circle[b].append(a)

for _ in range(M-1):
    x, y = read_ints()
    square[x].append(y)
    square[y].append(x)

def farthest(start, adj, n):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])
    far = start
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > dist[far]:
                    far = v
                q.append(v)
    return far, dist[far]

def get_diameter(adj, n):
    a, _ = farthest(1, adj, n)
    b, _ = farthest(a, adj, n)
    _, diam = farthest(b, adj, n)
    return b, a, diam

def get_centers(adj, n, end1, end2):
    dist1 = [-1] * (n+1)
    dist2 = [-1] * (n+1)
    q = deque()
    q.append(end1)
    dist1[end1] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist1[v] == -1:
                dist1[v] = dist1[u] + 1
                q.append(v)
    q.append(end2)
    dist2[end2] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist2[v] == -1:
                dist2[v] = dist2[u] + 1
                q.append(v)
    centers = []
    best = n + 5
    for i in range(1, n+1):
        d = max(dist1[i], dist2[i])
        if d < best:
            best = d
            centers = [i]
        elif d == best:
            centers.append(i)
    return centers

def main():
    if N == 1:
        print(1, 1)
        return
    if M == 1:
        print(1, 1)
        return

    e1c, e2c, diam_c = get_diameter(circle, N)
    e1s, e2s, diam_s = get_diameter(square, M)

    centers_c = get_centers(circle, N, e1c, e2c)
    centers_s = get_centers(square, M, e1s, e2s)

    best_d = 10**9
    best_pair = (1, 1)

    for cc in centers_c:
        for cs in centers_s:
            d1 = max(diam_c, diam_s)
            d2 = (diam_c + 1) // 2 + (diam_s + 1) // 2 + 1
            curr = max(d1, d2)
            if curr < best_d:
                best_d = curr
                best_pair = (cc, cs)

    print(best_pair[0], best_pair[1])

main()
