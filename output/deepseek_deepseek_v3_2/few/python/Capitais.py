import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    capitals = [i for i in range(1, n + 1) if degree[i] == 1]
    if len(capitals) == 2:
        print(1)
        return

    dist = [-1] * (n + 1)
    q = []
    for cap in capitals:
        dist[cap] = 0
        q.append(cap)

    diameter_end = q[0]
    max_dist = 0
    while q:
        u = q.pop()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > max_dist:
                    max_dist = dist[v]
                    diameter_end = v

    dist = [-1] * (n + 1)
    q = [diameter_end]
    dist[diameter_end] = 0
    max_dist = 0
    while q:
        u = q.pop()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > max_dist:
                    max_dist = dist[v]

    print((max_dist + 1) // 2)

if __name__ == "__main__":
    solve()