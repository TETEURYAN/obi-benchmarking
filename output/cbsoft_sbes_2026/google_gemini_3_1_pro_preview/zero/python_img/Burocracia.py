
import sys

# Aumentar o limite de recursão para árvores profundas e DSU
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    p = [0, 0] + [int(x) for x in input_data[1:N]]
    
    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        adj[p[i]].append(i)
        
    LOG = 18
    up = [[0] * (N + 1) for _ in range(LOG)]
    for i in range(2, N + 1):
        up[0][i] = p[i]
        
    for j in range(1, LOG):
        for i in range(1, N + 1):
            up[j][i] = up[j-1][up[j-1][i]]
            
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    node_at = [0] * (N + 1)
    timer = 0
    
    # DFS iterativa para evitar estouro de pilha e overhead de chamadas
    stack = [1]
    edge_idx = [0] * (N + 1)
    
    while stack:
        u = stack[-1]
        if edge_idx[u] == 0:
            timer += 1
            in_time[u] = timer
            node_at[timer] = u
            
        if edge_idx[u] < len(adj[u]):
            v = adj[u][edge_idx[u]]
            edge_idx[u] += 1
            stack.append(v)
        else:
            out_time[u] = timer
            stack.pop()
            
    bit = [0] * (N + 2)
    
    # Inicialização da Fenwick Tree (Binary Indexed Tree)
    for i in range(1, N + 1):
        idx_fen = in_time[i]
        while idx_fen <= N:
            bit[idx_fen] += 1
            idx_fen += idx_fen & (-idx_fen)
            
        idx_fen = out_time[i] + 1
        while idx_fen <= N:
            bit[idx_fen] -= 1
            idx_fen += idx_fen & (-idx_fen)
            
    dsu_parent = list(range(N + 2))
    def find(i):
        if dsu_parent[i] == i:
            return i
        dsu_parent[i] = find(dsu_parent[i])
        return dsu_parent[i]
        
    is_barren = [False] * (N + 1)
    
    idx = N
    Q = int(input_data[idx])
    idx += 1
    
    out_res = []
    
    for _ in range(Q):
        type = int(input_data[idx])
        if type == 1:
            v = int(input_data[idx+1])
            k = int(input_data[idx+2])
            idx += 3
            
            # Consulta S(v) na Fenwick Tree
            idx_fen = in_time[v]
            sv = 0
            while idx_fen > 0:
                sv += bit[idx_fen]
                idx_fen -= idx_fen & (-idx_fen)
                
            if is_barren[v]:
                target = sv - k + 1
            else:
                target = sv - k
                
            curr = v
            for j in range(LOG - 1, -1, -1):
                nxt = up[j][curr]
                if nxt != 0:
                    idx_fen = in_time[nxt]
                    s = 0
                    while idx_fen > 0:
                        s += bit[idx_fen]
                        idx_fen -= idx_fen & (-idx_fen)
                    if s >= target:
                        curr = nxt
            out_res.append(str(curr))
            
        else:
            v = int(input_data[idx+1])
            idx += 2
            
            if not is_barren[v]:
                curr_idx = find(in_time[v] + 1)
                end_idx = out_time[v]
                while curr_idx <= end_idx:
                    u = node_at[curr_idx]
                    is_barren[u] = True
                    
                    # Atualiza a Fenwick Tree para o nó que se tornou "estéril"
                    idx_fen = in_time[u]
                    while idx_fen <= N:
                        bit[idx_fen] -= 1
                        idx_fen += idx_fen & (-idx_fen)
                        
                    idx_fen = out_time[u] + 1
                    while idx_fen <= N:
                        bit[idx_fen] += 1
                        idx_fen += idx_fen & (-idx_fen)
                        
                    dsu_parent[curr_idx] = curr_idx + 1
                    curr_idx = find(curr_idx + 1)
                    
    sys.stdout.write('\n'.join(out_res) + '\n')

if __name__ == '__main__':
    solve()
