
import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    tokens = get_ints()
    
    try:
        N = next(tokens)
        M = next(tokens)
    except StopIteration:
        return
        
    out_adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = next(tokens)
        v = next(tokens)
        out_adj[u].append(v)
        
    out_set = [set(l) for l in out_adj]
    
    for u in range(1, N + 1):
        adj_u_list = out_adj[u]
        if not adj_u_list:
            continue
            
        set_u = out_set[u].copy()
        set_u.add(u)
        
        for v in adj_u_list:
            if not out_set[v].issubset(set_u):
                for w in out_adj[v]:
                    if w not in set_u:
                        print(f"{u} {w}")
                        return
                        
    print("-1")

if __name__ == '__main__':
    solve()
