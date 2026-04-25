import sys
sys.setrecursionlimit(200000)

def kosaraju(n, edges):
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        radj[b].append(a)

    visited = [False] * (n + 1)
    order = []

    def dfs1(v):
        visited[v] = True
        for to in adj[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * (n + 1)
    cur_comp = 0

    def dfs2(v):
        comp[v] = cur_comp
        for to in radj[v]:
            if comp[to] == -1:
                dfs2(to)

    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v)
            cur_comp += 1

    return comp, cur_comp

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    out_lines = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        edges = []
        for _ in range(n):
            a = int(next(it))
            b = int(next(it))
            edges.append((a, b))
        comp, num_comp = kosaraju(n, edges)
        if num_comp == 1:
            out_lines.append('S')
        else:
            out_lines.append('N')
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()