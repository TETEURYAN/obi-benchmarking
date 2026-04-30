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
        
    order = []
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    
    queue = [1]
    visited[1] = True
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
                
    size = [1] * (N + 1)
    
    for u in reversed(order):
        p = parent[u]
        if p != 0:
            size[p] += size[u]
            
    min_diff = float('inf')
    for i in range(2, N + 1):
        diff = abs(N - 2 * size[i])
        if diff < min_diff:
            min_diff = diff
            
    print(min_diff)

if __name__ == '__main__':
    solve()