import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n+1)]
    grau = [0]*(n+1)
    for _ in range(n-1):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        grau[u] += 1
        grau[v] += 1

    capital = [False]*(n+1)
    for i in range(1, n+1):
        if grau[i] == 1:
            capital[i] = True

    if n == 2:
        print(1)
        return

    raiz = 1
    parent = [0]*(n+1)
    down = [0]*(n+1)
    best1 = [10**9]*(n+1)
    best2 = [10**9]*(n+1)
    best1_child = [-1]*(n+1)

    def dfs1(v, p):
        parent[v] = p
        if capital[v]:
            down[v] = 0
        else:
            down[v] = 10**9
        for u in adj[v]:
            if u == p:
                continue
            dfs1(u, v)
            if not capital[v]:
                if down[u] + 1 < down[v]:
                    down[v] = down[u] + 1
            val = down[u] + 1
            if val < best1[v]:
                best2[v] = best1[v]
                best1[v] = val
                best1_child[v] = u
            elif val < best2[v]:
                best2[v] = val

    dfs1(raiz, 0)

    up = [10**9]*(n+1)
    up[raiz] = 10**9

    def dfs2(v, p):
        for u in adj[v]:
            if u == p:
                continue
            if capital[p]:
                up[u] = 1
            else:
                other = best1[v] if best1_child[v] != u else best2[v]
                candidate = 10**9
                if up[v] != 10**9:
                    candidate = min(candidate, up[v] + 1)
                if other != 10**9:
                    candidate = min(candidate, other + 1)
                up[u] = candidate
            dfs2(u, v)

    dfs2(raiz, 0)

    ans = 10**9
    for v in range(1, n+1):
        dists = []
        for u in adj[v]:
            if u == parent[v]:
                dists.append(up[v])
            else:
                dists.append(down[u] + 1)
        if len(dists) >= 2:
            dists.sort()
            ans = min(ans, dists[0] + dists[1])

    if ans == 10**9:
        ans = 1
    print(ans)

if __name__ == "__main__":
    main()