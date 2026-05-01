import sys

sys.setrecursionlimit(1_000_000)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    adj = [[] for _ in range(N + 1)]
    edges = set()
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
        if a > b:
            a, b = b, a
        edges.add((a, b))
    
    comp = [-1] * (N + 1)
    comps = []
    
    cid = 0
    for s in range(1, N + 1):
        if comp[s] != -1:
            continue
        stack = [s]
        comp[s] = cid
        nodes = []
        while stack:
            u = stack.pop()
            nodes.append(u)
            for v in adj[u]:
                if comp[v] == -1:
                    comp[v] = cid
                    stack.append(v)
        comps.append(nodes)
        cid += 1
    
    if len(comps) >= 2:
        print(comps[0][0], comps[1][0])
        return
    
    nodes = comps[0]
    if len(nodes) <= 1:
        print(-1)
        return
    
    deg = [0] * (N + 1)
    for u in nodes:
        deg[u] = len(adj[u])
    
    if any(deg[u] < len(nodes) - 1 for u in nodes):
        mark = [False] * (N + 1)
        for u in nodes:
            if deg[u] == len(nodes) - 1:
                continue
            for v in adj[u]:
                mark[v] = True
            mark[u] = True
            for w in nodes:
                if not mark[w]:
                    print(u, w)
                    return
            for v in adj[u]:
                mark[v] = False
            mark[u] = False
    
    print(-1)

if __name__ == "__main__":
    main()