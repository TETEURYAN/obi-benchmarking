import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    adj = [[] for _ in range(n)]
    deg = [0] * n

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    leaves = [i for i in range(n) if deg[i] == 1]

    if len(leaves) <= 1:
        print(0)
        return

    dist = [-1] * n
    owner = [-1] * n
    q = deque()

    for leaf in leaves:
        dist[leaf] = 0
        owner[leaf] = leaf
        q.append(leaf)

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
