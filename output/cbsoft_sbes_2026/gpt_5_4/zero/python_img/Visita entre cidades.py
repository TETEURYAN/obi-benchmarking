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
        p, q, d = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        adj[p].append((q, d))
        adj[q].append((p, d))

    dist = [-1] * (n + 1)
    dist[a] = 0
    q = deque([a])

    while q:
        u = q.popleft()
        if u == b:
            break
        for v, w in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                q.append(v)

    print(dist[b])

if __name__ == "__main__":
    main()