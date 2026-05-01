import sys

def solve():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
                
    tokens = get_tokens()
    
    try:
        S_str = next(tokens)
    except StopIteration:
        return
    S = int(S_str)
    T = int(next(tokens))
    
    adj = [[False] * (S + 1) for _ in range(S + 1)]
    
    for _ in range(T):
        u = int(next(tokens))
        v = int(next(tokens))
        adj[u][v] = True
        adj[v][u] = True
        
    P = int(next(tokens))
    
    possible_count = 0
    for _ in range(P):
        N = int(next(tokens))
        if N > 0:
            prev = int(next(tokens))
            possible = True
            for _ in range(1, N):
                curr = int(next(tokens))
                if not adj[prev][curr]:
                    possible = False
                prev = curr
            if possible:
                possible_count += 1
                
    print(possible_count)

if __name__ == '__main__':
    solve()