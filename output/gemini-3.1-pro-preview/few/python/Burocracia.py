import sys

# Aumentar o limite de recursão por precaução, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    p = [0] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    
    idx = 1
    for i in range(2, N + 1):
        p[i] = int(input_data[idx])
        adj[p[i]].append(i)
        idx += 1
        
    Q = int(input_data[idx])
    idx += 1
    
    LOG = 18
    up = [[0] * LOG for _ in range(N + 1)]
    depth = [0] * (N + 1)
    
    # Pré-computar profundidades e binary lifting iterativamente
    for i in range(2, N + 1):
        u = p[i]
        depth[i] = depth[u] + 1
        up[i][0] = u
        for j in range(1, LOG):
            up[i][j] = up[up[i][j-1]][j-1]
            
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    timer = 0
    
    # DFS iterativa para calcular in_time e out_time
    stack = [1]
    edge_idx = [0] * (N + 1)
    
    while stack:
        u = stack[-1]
        if edge_idx[u] == 0:
            timer += 1
            in_time[u] = timer
            
        if edge_idx[u] < len(adj[u]):
            v = adj[u][edge_idx[u]]
            edge_idx[u] += 1
            stack.append(v)
        else:
            out_time[u] = timer
            stack.pop()
            
    # Segment Tree iterativa para Range Update e Point Query
    M = N + 2
    tree_depth = [10**9] * (2 * M)
    tree_node = [-1] * (2 * M)
    
    def update(l, r, d, u):
        if l > r:
            return
        l += M
        r += M + 1
        while l < r:
            if l % 2 == 1:
                if d < tree_depth[l]:
                    tree_depth[l] = d
                    tree_node[l] = u
                l += 1
            if r % 2 == 1:
                r -= 1
                if d < tree_depth[r]:
                    tree_depth[r] = d
                    tree_node[r] = u
            l //= 2
            r //= 2
            
    def query(pos):
        pos += M
        ans_d = 10**9
        ans_u = -1
        while pos > 0:
            if tree_depth[pos] < ans_d:
                ans_d = tree_depth[pos]
                ans_u = tree_node[pos]
            pos //= 2
        return ans_u
        
    out = []
    for _ in range(Q):
        type_op = int(input_data[idx])
        if type_op == 1:
            v = int(input_data[idx+1])
            k = int(input_data[idx+2])
            idx += 3
            
            H_v = query(in_time[v])
            if H_v != -1:
                if k == 1:
                    ans = H_v
                else:
                    curr = H_v
                    rem = k - 1
                    j = 0
                    while rem > 0:
                        if rem & 1:
                            curr = up[curr][j]
                        rem >>= 1
                        j += 1
                    ans = curr
            else:
                curr = v
                rem = k
                j = 0
                while rem > 0:
                    if rem & 1:
                        curr = up[curr][j]
                    rem >>= 1
                    j += 1
                ans = curr
            out.append(str(ans))
        else:
            v = int(input_data[idx+1])
            idx += 2
            # Atualiza a subárvore estrita de v
            update(in_time[v] + 1, out_time[v], depth[v], v)
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()