from collections import deque

def find_path(adj, start, end, n):
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    
    return path

def main():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * (N + 1)
    
    for _ in range(M):
        p = int(input_data[idx]); idx += 1
        q = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        
        path = find_path(adj, p, q, N)
        for castle in path:
            colors[castle] = c
    
    print(' '.join(str(colors[i]) for i in range(1, N + 1)))

main()