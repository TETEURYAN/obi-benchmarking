import sys
from collections import deque

def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    # Primeira BFS para encontrar A
    dist0 = bfs(1, adj, n)
    A = 1
    for i in range(1, n + 1):
        if dist0[i] > dist0[A]:
            A = i

    # Segunda BFS a partir de A para encontrar B e dA
    dA = bfs(A, adj, n)
    B = A
    for i in range(1, n + 1):
        if dA[i] > dA[B]:
            B = i

    # Terceira BFS a partir de B para dB
    dB = bfs(B, adj, n)

    D = dA[B]

    pos = neg = zero = 0
    for v in range(1, n + 1):
        if max(dA[v], dB[v]) == D:
            delta = dA[v] - dB[v]
            if delta > 0:
                pos += 1
            elif delta < 0:
                neg += 1
            else:
                zero += 1

    pairs = zero * (zero - 1) // 2 + zero * (pos + neg) + pos * neg

    print(D + 1)
    print(pairs)

if __name__ == "__main__":
    main()