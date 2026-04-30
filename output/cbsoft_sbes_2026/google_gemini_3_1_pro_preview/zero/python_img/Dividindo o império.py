
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    adj = [[] for _ in range(N + 1)]
    idx = 1
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    parent = [0] * (N + 1)
    order = []
    stack = [1]
    visited = [False] * (N + 1)
    visited[1] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)
                
    size = [1] * (N + 1)
    min_diff = float('inf')
    
    for i in range(N - 1, -1, -1):
        u = order[i]
        p = parent[u]
        if p != 0:
            size[p] += size[u]
            diff = abs(N - 2 * size[u])
            if diff < min_diff:
                min_diff = diff
                
    print(min_diff)

if __name__ == '__main__':
    solve()
