import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    colors = [0] * (n + 1)
    for i in range(1, n + 1):
        colors[i] = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    size = [0] * (n + 1)
    heavy = [-1] * (n + 1)
    
    def dfs(v, p):
        parent[v] = p
        size[v] = 1
        max_size = 0
        for to in adj[v]:
            if to == p:
                continue
            depth[to] = depth[v] + 1
            dfs(to, v)
            size[v] += size[to]
            if size[to] > max_size:
                max_size = size[to]
                heavy[v] = to
    dfs(1, 0)
    
    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    cur_pos = 0
    
    def decompose(v, h):
        nonlocal cur_pos
        head[v] = h
        pos[v] = cur_pos
        cur_pos += 1
        if heavy[v] != -1:
            decompose(heavy[v], h)
        for to in adj[v]:
            if to != parent[v] and to != heavy[v]:
                decompose(to, to)
    decompose(1, 1)
    
    bit = [0] * (n + 2)
    def bit_add(idx, delta):
        i = idx + 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i
    def bit_sum(idx):
        s = 0
        i = idx + 1
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s
    def bit_range_sum(l, r):
        return bit_sum(r) - bit_sum(l - 1)
    
    color_positions = [[] for _ in range(n // 2 + 1)]
    for v in range(1, n + 1):
        color_positions[colors[v]].append(v)
    
    total = 0
    for c in range(1, n // 2 + 1):
        u, v = color_positions[c]
        res = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            res += depth[u] - depth[head[u]] + 1
            u = parent[head[u]]
        if depth[u] > depth[v]:
            u, v = v, u
        res += depth[v] - depth[u]
        total += res
    
    print(total)

if __name__ == "__main__":
    solve()