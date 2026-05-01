import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = {i: [] for i in range(1, N + 1)}
    
    idx = 2
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    colors = [0] * (N + 1)
    
    for _ in range(M):
        p = int(input_data[idx])
        q = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        queue = [p]
        parent = {p: -1}
        while queue:
            curr = queue.pop(0)
            if curr == q:
                break
            for neighbor in adj[curr]:
                if neighbor not in parent:
                    parent[neighbor] = curr
                    queue.append(neighbor)
        
        curr = q
        while curr != -1:
            colors[curr] = c
            curr = parent[curr]
            
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()