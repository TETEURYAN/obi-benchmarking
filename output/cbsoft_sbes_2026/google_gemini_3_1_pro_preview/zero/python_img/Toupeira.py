import sys

def solve():
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
                
    token_iter = get_ints()
    
    try:
        S = next(token_iter)
        T = next(token_iter)
    except StopIteration:
        return
        
    adj = [[False] * (S + 1) for _ in range(S + 1)]
    
    for _ in range(T):
        u = next(token_iter)
        v = next(token_iter)
        adj[u][v] = True
        adj[v][u] = True
        
    P = next(token_iter)
    
    valid_count = 0
    for _ in range(P):
        N = next(token_iter)
        walk = [next(token_iter) for _ in range(N)]
        
        is_valid = True
        for i in range(N - 1):
            if not adj[walk[i]][walk[i+1]]:
                is_valid = False
                break
        
        if is_valid:
            valid_count += 1
            
    print(valid_count)

if __name__ == '__main__':
    solve()