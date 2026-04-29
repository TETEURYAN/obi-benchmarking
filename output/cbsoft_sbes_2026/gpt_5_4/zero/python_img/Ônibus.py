import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, a, b = data[0], data[1], data[2]
    adj = [[] for _ in range(n + 1)]

    idx = 3
    for _ in range(n - 1):
        p, q = data[idx], data[idx + 1]
        idx += 2
        adj[p].append(q)
        adj[q].append(p)

    dist = [-1] * (n + 1)
    dist[a] = 0
    q = deque([a])

    while q:
        u = q.popleft()
        if u == b:
            print(dist[u])
            return
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

if __name__ == "__main__":
    main()
