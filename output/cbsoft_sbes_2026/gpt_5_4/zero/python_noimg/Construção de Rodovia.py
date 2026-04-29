import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    parent = list(range(N + 1))
    size = [1] * (N + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
        union(a, b)

    comp_vertices = {}
    for v in range(1, N + 1):
        r = find(v)
        if r not in comp_vertices:
            comp_vertices[r] = []
        comp_vertices[r].append(v)

    comp_edge_count = {}
    for a, b in edges:
        r = find(a)
        comp_edge_count[r] = comp_edge_count.get(r, 0) + 1

    for r, verts in comp_vertices.items():
        k = len(verts)
        e = comp_edge_count.get(r, 0)
        if e < k * (k - 1) // 2:
            mark = set(verts)
            adj = {v: set() for v in verts}
            for a, b in edges:
                if a in mark:
                    adj[a].add(b)
                    adj[b].add(a)
            for v in verts:
                if len(adj[v]) < k - 1:
                    for u in verts:
                        if u != v and u not in adj[v]:
                            print(v, u)
                            return

    print(-1)

if __name__ == "__main__":
    main()
