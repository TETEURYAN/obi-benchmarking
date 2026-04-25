import sys

def bfs(start, adj):
    dist = [-1] * (len(adj))
    q = [start]
    dist[start] = 0
    for u in q:
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def main():
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    out_lines = []
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        if n == 1:
            out_lines.append(f"Teste {test_num}\n1\n")
            test_num += 1
            continue
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            adj[x].append(y)
            adj[y].append(x)
        dist1 = bfs(1, adj)
        farthest = max(range(1, n + 1), key=lambda v: dist1[v])
        dist2 = bfs(farthest, adj)
        farthest2 = max(range(1, n + 1), key=lambda v: dist2[v])
        diameter = dist2[farthest2]
        # find center(s)
        path = []
        q = [farthest2]
        parent = [-1] * (n + 1)
        parent[farthest2] = 0
        for u in q:
            if u == farthest:
                break
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        node = farthest
        while node != 0:
            path.append(node)
            node = parent[node]
        mid = diameter // 2
        if diameter % 2 == 0:
            center = path[mid]
        else:
            center1 = path[mid]
            center2 = path[mid + 1]
            center = min(center1, center2)
        out_lines.append(f"Teste {test_num}\n{center}\n")
        test_num += 1
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()