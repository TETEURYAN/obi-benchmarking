import sys

sys.setrecursionlimit(200000)

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    edges = []
    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((c, u, v))
        except StopIteration:
            break
            
    edges.sort()
    
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        if root_i != root_j:
            if rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            elif rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False
    
    total_cost = 0
    edges_used = 0
    
    for c, u, v in edges:
        if union(u, v):
            total_cost += c
            edges_used += 1
            if edges_used == N - 1:
                break
                
    print(total_cost)

if __name__ == '__main__':
    main()