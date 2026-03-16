
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    p = [0, 0] + [int(x) for x in data[1:N]]
    
    LOG = 18
    up = [0] * ((N + 1) * LOG)
    for i in range(2, N + 1):
        up[i * LOG + 0] = p[i]
        for j in range(1, LOG):
            up[i * LOG + j] = up[up[i * LOG + (j - 1)] * LOG + (j - 1)]
            
    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        adj[p[i]].append(i)
        
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    timer = 0
    
    stack = [(1, 0)]
    while stack:
        u, state = stack.pop()
        if state == 1:
            out_time[u] = timer
        else:
            in_time[u] = timer
            timer += 1
            stack.append((u, 1))
            for v in reversed(adj[u]):
                stack.append((v, 0))
                
    time_tree = [-1] * (2 * N)
    val_tree = [0] * (2 * N)
    current_time = 0

    def update(l, r, val):
        nonlocal current_time
        current_time += 1
        l += N
        r += N
        while l < r:
            if l % 2 == 1:
                time_tree[l] = current_time
                val_tree[l] = val
                l += 1
            if r % 2 == 1:
                r -= 1
                time_tree[r] = current_time
                val_tree[r] = val
            l //= 2
            r //= 2

    def query_seg_tree(pos):
        pos += N
        max_time = -1
        res = 0
        while pos > 0:
            if time_tree[pos] > max_time:
                max_time = time_tree[pos]
                res = val_tree[pos]
            pos //= 2
        return res

    def get_kth_ancestor(u, k):
        for j in range(LOG):
            if (k >> j) & 1:
                u = up[u * LOG + j]
                if u == 0:
                    break
        return u

    Q = int(data[N])
    idx = N + 1
    out = []
    
    for _ in range(Q):
        type = int(data[idx])
        if type == 1:
            v = int(data[idx+1])
            k = int(data[idx+2])
            idx += 3
            
            parent_v = p[v]
            if parent_v != 0:
                h_inc_parent = query_seg_tree(in_time[parent_v])
                if h_inc_parent == 0:
                    ans = get_kth_ancestor(v, k)
                else:
                    if k == 1:
                        ans = h_inc_parent
                    else:
                        ans = get_kth_ancestor(h_inc_parent, k - 1)
                out.append(str(ans))
        else:
            v = int(data[idx+1])
            idx += 2
            
            h_inc_v = query_seg_tree(in_time[v])
            if h_inc_v == 0:
                update(in_time[v], out_time[v], v)
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
