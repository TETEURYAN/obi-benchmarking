import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    edges = []
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, v))
        idx += 3
        
    edges.sort()
    
    parent = list(range(N))
    rank = [0] * N
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False
        
    mst_cost = 0
    edges_added = 0
    
    for w, u, v in edges:
        if union(u, v):
            mst_cost += w
            edges_added += 1
            if edges_added == N - 1:
                break
                
    print(mst_cost)

if __name__ == '__main__':
    solve()