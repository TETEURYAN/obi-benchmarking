
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
            
    order = []
    parent = [0] * (N + 1)
    
    queue = [root]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                queue.append(v)
                
    min_dist = [float('inf')] * (N + 1)
    ans = float('inf')
    
    for u in reversed(order):
        if len(adj[u]) == 1:
            min_dist[u] = 0
        else:
            m1 = float('inf')
            m2 = float('inf')
            for v in adj[u]:
                if v != parent[u]:
                    d = min_dist[v] + 1
                    if d < m1:
                        m2 = m1
                        m1 = d
                    elif d < m2:
                        m2 = d
            min_dist[u] = m1
            if m2 != float('inf'):
                if m1 + m2 < ans:
                    ans = m1 + m2
                    
    print(ans)

if __name__ == '__main__':
    solve()
