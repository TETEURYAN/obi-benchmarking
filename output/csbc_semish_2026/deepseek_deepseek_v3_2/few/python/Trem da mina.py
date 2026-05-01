import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    E = int(next(it))
    R = int(next(it))
    
    adj = [[] for _ in range(E + 1)]
    edges = {}
    
    for _ in range(R):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        adj[a].append((b, c))
        adj[b].append((a, c))
        edges[(min(a, b), max(a, b))] = c
    
    K = int(next(it))
    queries = []
    for _ in range(K):
        x = int(next(it))
        t = int(next(it))
        queries.append((x, t))
    
    visited = [0] * (E + 1)
    parent = [0] * (E + 1)
    depth = [0] * (E + 1)
    dist_to_root = [0] * (E + 1)
    cycle_id = [0] * (E + 1)
    cycle_nodes = []
    cycles = []
    cycle_length = []
    
    def dfs(u, p):
        visited[u] = 1
        for v, w in adj[u]:
            if v == p:
                continue
            if visited[v] == 0:
                parent[v] = u
                depth[v] = depth[u] + 1
                dist_to_root[v] = dist_to_root[u] + w
                dfs(v, u)
            elif visited[v] == 1 and depth[v] < depth[u]:
                nodes = []
                cur = u
                while cur != v:
                    nodes.append(cur)
                    cur = parent[cur]
                nodes.append(v)
                cycles.append(nodes[:])
                cid = len(cycles)
                for node in nodes:
                    cycle_id[node] = cid
    
        visited[u] = 2
    
    for i in range(1, E + 1):
        if not visited[i]:
            dfs(i, 0)
    
    for cycle in cycles:
        total = 0
        n = len(cycle)
        for i in range(n):
            a = cycle[i]
            b = cycle[(i + 1) % n]
            total += edges[(min(a, b), max(a, b))]
        cycle_length.append(total)
    
    INF = 10**18
    dist = [[INF, INF] for _ in range(E + 1)]
    from collections import deque
    
    for i in range(1, E + 1):
        if cycle_id[i] != 0:
            q = deque()
            dist[i][0] = 0
            q.append((i, 0))
            while q:
                u, parity = q.popleft()
                for v, w in adj[u]:
                    if cycle_id[v] == cycle_id[i]:
                        new_parity = parity ^ 1
                        if dist[v][new_parity] > dist[u][parity] + w:
                            dist[v][new_parity] = dist[u][parity] + w
                            q.append((v, new_parity))
    
    out_lines = []
    for x, t in queries:
        if cycle_id[x] == 0:
            out_lines.append("-1")
            continue
        
        cid = cycle_id[x] - 1
        cycle = cycles[cid]
        total_len = cycle_length[cid]
        
        if t > total_len:
            out_lines.append("-1")
            continue
        
        best = INF
        for parity in (0, 1):
            d = dist[x][parity]
            if d >= INF:
                continue
            if parity == 0:
                if t % 2 == 0:
                    best = min(best, d + (t // 2) * total_len)
            else:
                if t % 2 == 1:
                    best = min(best, d + (t // 2) * total_len)
        
        if best >= INF:
            out_lines.append("-1")
        else:
            out_lines.append(str(best * 2))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()