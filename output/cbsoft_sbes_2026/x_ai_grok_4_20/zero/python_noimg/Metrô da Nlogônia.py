
import sys
sys.setrecursionlimit(400000)

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

N, M = read_ints()

adj_c = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = read_ints()
    adj_c[a].append(b)
    adj_c[b].append(a)

adj_q = [[] for _ in range(M+1)]
for _ in range(M-1):
    x, y = read_ints()
    adj_q[x].append(y)
    adj_q[y].append(x)

def farthest(start, adj, n):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = [start]
    far = start
    for u in q:
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > dist[far]:
                    far = v
                q.append(v)
    return far, dist[far]

def get_diameter(adj, n):
    u, _ = farthest(1, adj, n)
    v, diam = farthest(u, adj, n)
    return u, v, diam

# Find centers for Circle
u1, v1, diam_c = get_diameter(adj_c, N)
dist_u = [-1] * (N+1)
dist_v = [-1] * (N+1)
q = [u1]
dist_u[u1] = 0
for uu in q:
    for vv in adj_c[uu]:
        if dist_u[vv] == -1:
            dist_u[vv] = dist_u[uu] + 1
            q.append(vv)
q = [v1]
dist_v[v1] = 0
for uu in q:
    for vv in adj_c[uu]:
        if dist_v[vv] == -1:
            dist_v[vv] = dist_v[uu] + 1
            q.append(vv)

centers_c = []
for i in range(1, N+1):
    if abs(dist_u[i] - dist_v[i]) <= 1 and dist_u[i] + dist_v[i] == diam_c:
        centers_c.append(i)

# Find centers for Square
u2, v2, diam_q = get_diameter(adj_q, M)
dist_u = [-1] * (M+1)
dist_v = [-1] * (M+1)
q = [u2]
dist_u[u2] = 0
for uu in q:
    for vv in adj_q[uu]:
        if dist_u[vv] == -1:
            dist_u[vv] = dist_u[uu] + 1
            q.append(vv)
q = [v2]
dist_v[v2] = 0
for uu in q:
    for vv in adj_q[uu]:
        if dist_v[vv] == -1:
            dist_v[vv] = dist_v[uu] + 1
            q.append(vv)

centers_q = []
for i in range(1, M+1):
    if abs(dist_u[i] - dist_v[i]) <= 1 and dist_u[i] + dist_v[i] == diam_q:
        centers_q.append(i)

# The optimal connection is between any center of C and any center of Q
print(centers_c[0], centers_q[0])
