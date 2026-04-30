import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    edges = []
    idx = 2
    for _ in range(M):
        edges.append((int(input_data[idx+2]), int(input_data[idx]), int(input_data[idx+1])))
        idx += 3
        
    edges.sort()
    
    parent = list(range(N + 1))
    
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        curr = i
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
        return root

    total_cost = 0
    edges_used = 0
    
    if N == 1:
        print(0)
        return
        
    for c, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            total_cost += c
            edges_used += 1
            if edges_used == N - 1:
                break
                
    print(total_cost)

if __name__ == '__main__':
    solve()