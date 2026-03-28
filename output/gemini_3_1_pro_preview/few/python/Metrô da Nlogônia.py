import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj_circle = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_circle[u].append(v)
        adj_circle[v].append(u)
        idx += 2
        
    adj_square = [[] for _ in range(m + 1)]
    for _ in range(m - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj_square[u].append(v)
        adj_square[v].append(u)
        idx += 2
        
    def get_center(nodes, adj):
        dist = [-1] * (nodes + 1)
        q = [1]
        dist[1] = 0
        farthest_node = 1
        max_d = 0
        
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > max_d:
                        max_d = dist[v]
                        farthest_node = v
                        
        A = farthest_node
        
        dist = [-1] * (nodes + 1)
        parent = [-1] * (nodes + 1)
        q = [A]
        dist[A] = 0
        farthest_node = A
        max_d = 0
        
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                    if dist[v] > max_d:
                        max_d = dist[v]
                        farthest_node = v
                        
        B = farthest_node
        
        path = []
        curr = B
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
            
        return path[len(path) // 2]

    center_circle = get_center(n, adj_circle)
    center_square = get_center(m, adj_square)
    
    print(f"{center_circle} {center_square}")

if __name__ == '__main__':
    solve()