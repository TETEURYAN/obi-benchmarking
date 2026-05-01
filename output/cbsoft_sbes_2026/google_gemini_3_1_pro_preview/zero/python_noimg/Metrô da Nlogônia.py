import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj_N = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_N[u].append(v)
        adj_N[v].append(u)
        idx += 2
        
    adj_M = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_M[u].append(v)
        adj_M[v].append(u)
        idx += 2
        
    def get_center(n, adj):
        dist = [-1] * (n + 1)
        q = [1]
        dist[1] = 0
        farthest_node = 1
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    farthest_node = v
                    
        A = farthest_node
        
        dist = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        q = [A]
        dist[A] = 0
        farthest_node = A
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                    farthest_node = v
                    
        B = farthest_node
        
        path = []
        curr = B
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
            
        return path[len(path) // 2]

    center_N = get_center(N, adj_N)
    center_M = get_center(M, adj_M)
    
    print(f"{center_N} {center_M}")

if __name__ == '__main__':
    solve()