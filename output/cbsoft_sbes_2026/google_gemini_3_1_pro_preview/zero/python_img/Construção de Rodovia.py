
import sys

def solve():
    def get_ints():
        for token in sys.stdin.read().split():
            yield int(token)
            
    token_iter = get_ints()
    
    try:
        N = next(token_iter)
        M = next(token_iter)
    except StopIteration:
        return
        
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = next(token_iter)
        v = next(token_iter)
        adj[u].append(v)
        adj[v].append(u)
        
    visited = bytearray(N + 1)
    
    for i in range(1, N + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = 1
            
            edges_count = 0
            
            while stack:
                u = stack.pop()
                comp.append(u)
                edges_count += len(adj[u])
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = 1
                        stack.append(v)
                        
            k = len(comp)
            e = edges_count // 2
            
            if e < k * (k - 1) // 2:
                for u in comp:
                    if len(adj[u]) < k - 1:
                        neighbors = set(adj[u])
                        for v in comp:
                            if v != u and v not in neighbors:
                                print(f"{u} {v}")
                                return
                                
    print("-1")

if __name__ == '__main__':
    solve()
