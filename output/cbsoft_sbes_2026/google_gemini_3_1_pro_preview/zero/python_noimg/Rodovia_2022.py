
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    
    out_set = [set() for _ in range(N + 1)]
    in_edges = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        out_set[u].add(v)
        in_edges[v].append(u)
        
    for C in range(1, N + 1):
        set_C = out_set[C]
        if not set_C:
            continue
        for A in in_edges[C]:
            # Adiciona A temporariamente para lidar com ciclos de tamanho 2
            out_set[A].add(A)
            is_sub = set_C.issubset(out_set[A])
            out_set[A].remove(A)
            
            if not is_sub:
                for B in set_C:
                    if B != A and B not in out_set[A]:
                        print(f"{A} {B}")
                        return
                        
    print("-1")

if __name__ == '__main__':
    solve()
