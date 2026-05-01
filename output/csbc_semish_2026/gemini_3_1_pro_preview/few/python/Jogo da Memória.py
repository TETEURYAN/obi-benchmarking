import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    pos = [[] for _ in range(n // 2 + 1)]
    for i in range(1, n + 1):
        label = int(input_data[i])
        pos[label].append(i)
        
    adj = [[] for _ in range(n + 1)]
    idx = n + 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    LOG = 17
    up = [[0] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)
    
    queue = [1]
    head = 0
    visited = [False] * (n + 1)
    visited[1] = True
    
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[v][0] = u
                queue.append(v)
                
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if up[i][j-1] != 0:
                up[i][j] = up[up[i][j-1]][j-1]
                
    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for j in range(LOG):
            if (diff >> j) & 1:
                u = up[u][j]
                
        if u == v:
            return u
            
        for j in range(LOG - 1, -1, -1):
            if up[u][j] != up[v][j]:
                u = up[u][j]
                v = up[v][j]
                
        return up[u][0]
        
    total_dist = 0
    for i in range(1, n // 2 + 1):
        u = pos[i][0]
        v = pos[i][1]
        lca = get_lca(u, v)
        total_dist += depth[u] + depth[v] - 2 * depth[lca]
        
    print(total_dist)

if __name__ == '__main__':
    solve()