
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    if N == 2:
        print(1)
        return
        
    adj = [[] for _ in range(N + 1)]
    idx = 1
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    root = 1
    for i in range(1, N + 1):
        if len(adj[i]) >= 2:
            root = i
            break
            
    stack = [root]
    parent = [0] * (N + 1)
    order = []
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
                
    min_depth = [float('inf')] * (N + 1)
    ans = float('inf')
    
    for u in reversed(order):
        is_leaf = True
        for v in adj[u]:
            if v != parent[u]:
                is_leaf = False
                if min_depth[u] != float('inf'):
                    if min_depth[u] + min_depth[v] + 1 < ans:
                        ans = min_depth[u] + min_depth[v] + 1
                if min_depth[v] + 1 < min_depth[u]:
                    min_depth[u] = min_depth[v] + 1
        if is_leaf:
            min_depth[u] = 0
            
    print(ans)

if __name__ == '__main__':
    solve()
