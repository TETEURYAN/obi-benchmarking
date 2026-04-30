import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj1 = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj1[u].append(v)
        adj1[v].append(u)
        idx += 2
        
    adj2 = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj2[u].append(v)
        adj2[v].append(u)
        idx += 2
        
    def get_farthest_and_parents(start, adj, n):
        dist = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        dist[start] = 0
        q = [start]
        farthest_node = start
        max_dist = 0
        
        for u in q:
            if dist[u] > max_dist:
                max_dist = dist[u]
                farthest_node = u
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                    
        return farthest_node, parent

    def get_center(adj, n):
        if n == 1:
            return 1
        A, _ = get_farthest_and_parents(1, adj, n)
        B, parent = get_farthest_and_parents(A, adj, n)
        
        path = []
        curr = B
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
            
        return path[len(path) // 2]

    center1 = get_center(adj1, N)
    center2 = get_center(adj2, M)
    
    print(f"{center1} {center2}")

if __name__ == '__main__':
    solve()