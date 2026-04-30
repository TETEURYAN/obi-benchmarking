import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    p = [0] * (N + 1)
    for i in range(2, N + 1):
        p[i] = int(data[i - 1])
        
    Q_idx = N
    Q = int(data[Q_idx])
    
    LOG = 18
    up = [0] * ((N + 1) * LOG)
    depth = [0] * (N + 1)
    
    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        up[i * LOG + 0] = p[i]
        adj[p[i]].append(i)
        
    for i in range(2, N + 1):
        depth[i] = depth[p[i]] + 1
        for j in range(1, LOG):
            prev = up[i * LOG + j - 1]
            up[i * LOG + j] = up[prev * LOG + j - 1]
            
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    
    edge_idx = [0] * (N + 1)
    stack = [1]
    timer = 0
    in_time[1] = timer
    timer += 1
    
    while stack:
        u = stack[-1]
        if edge_idx[u] < len(adj[u]):
            v = adj[u][edge_idx[u]]
            edge_idx[u] += 1
            in_time[v] = timer
            timer += 1
            stack.append(v)
        else:
            out_time[u] = timer - 1
            stack.pop()
            
    INF = 10**9
    M = N + 1
    tree = [INF] * (2 * M)
    
    def update(l, r, val):
        l += M
        r += M + 1
        while l < r:
            if l % 2 == 1:
                if val < tree[l]: tree[l] = val
                l += 1
            if r % 2 == 1:
                r -= 1
                if val < tree[r]: tree[r] = val
            l //= 2
            r //= 2

    def query(pos):
        pos += M
        res = INF
        while pos > 0:
            if tree[pos] < res: res = tree[pos]
            pos //= 2
        return res

    def get_kth_ancestor(u, k):
        for j in range(LOG):
            if (k >> j) & 1:
                u = up[u * LOG + j]
        return u

    idx = Q_idx + 1
    out = []
    for _ in range(Q):
        type = int(data[idx])
        if type == 1:
            v = int(data[idx+1])
            k = int(data[idx+2])
            idx += 3
            
            pv = p[v]
            d = query(in_time[pv])
            if d == INF:
                ans = get_kth_ancestor(v, k)
            else:
                diff = depth[pv] - d
                y = pv
                if diff > 0:
                    y = get_kth_ancestor(pv, diff)
                if k == 1:
                    ans = y
                else:
                    ans = get_kth_ancestor(y, k - 1)
            out.append(str(ans))
        else:
            v = int(data[idx+1])
            idx += 2
            update(in_time[v], out_time[v], depth[v])
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()