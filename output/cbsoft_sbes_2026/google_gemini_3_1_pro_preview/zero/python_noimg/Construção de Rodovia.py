import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (N + 1)
    
    for i in range(1, N + 1):
        if not visited[i]:
            comp = []
            queue = [i]
            visited[i] = True
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            
            Vc = len(comp)
            if Vc <= 1:
                continue
                
            Ec = sum(len(adj[u]) for u in comp) // 2
            
            if Ec < Vc * (Vc - 1) // 2:
                for u in comp:
                    if len(adj[u]) < Vc - 1:
                        neighbors = set(adj[u])
                        for v in comp:
                            if v != u and v not in neighbors:
                                print(f"{u} {v}")
                                return
                                
    print("-1")

if __name__ == '__main__':
    solve()