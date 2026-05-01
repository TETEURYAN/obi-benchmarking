import sys
from collections import deque

def main():
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
        return

    capitals = [deg[i] == 1 for i in range(N)]

    dist = [-1] * N
    owner = [-1] * N
    q = deque()

    for i in range(N):
        if capitals[i]:
            dist[i] = 0
            owner[i] = i
            q.append(i)

    ans = 10**18

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                owner[v] = owner[u]
                q.append(v)
            elif owner[v] != owner[u]:
                cand = dist[u] + dist[v] + 1
                if cand < ans:
                    ans = cand

    print(ans)

if __name__ == "__main__":
    main()
