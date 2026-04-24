import sys
sys.setrecursionlimit(200000)

def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y, parent, size):
    rx = find(x, parent)
    ry = find(y, parent)
    if rx == ry:
        return
    if size[rx] < size[ry]:
        parent[rx] = ry
        size[ry] += size[rx]
    else:
        parent[ry] = rx
        size[rx] += size[ry]

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    B = int(next(it))
    
    edges = []
    for _ in range(B):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((w, u, v))
    
    edges.sort(reverse=True)
    
    parent = list(range(N))
    size = [1] * N
    queries = []
    C = int(next(it))
    for idx in range(C):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        queries.append((x, y, idx))
    
    result = [0] * C
    active = [False] * C
    adj_queries = [[] for _ in range(N)]
    for x, y, idx in queries:
        if x == y:
            result[idx] = 10**9
        else:
            adj_queries[x].append((y, idx))
            adj_queries[y].append((x, idx))
            active[idx] = True
    
    edge_idx = 0
    for w, u, v in edges:
        while edge_idx < B and edges[edge_idx][0] >= w:
            cu, cv = edges[edge_idx][1], edges[edge_idx][2]
            ru = find(cu, parent)
            rv = find(cv, parent)
            if ru != rv:
                if size[ru] < size[rv]:
                    ru, rv = rv, ru
                parent[rv] = ru
                size[ru] += size[rv]
                
                stack = []
                for node in [rv]:
                    stack.append(node)
                while stack:
                    node = stack.pop()
                    for neigh, qid in adj_queries[node]:
                        if active[qid] and find(neigh, parent) == ru:
                            result[qid] = w
                            active[qid] = False
                    adj_queries[node] = []
            edge_idx += 1
    
    for idx in range(C):
        if active[idx]:
            result[idx] = 0
    
    out_lines = []
    for val in result:
        out_lines.append(str(val))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()