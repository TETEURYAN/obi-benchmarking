import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = int(input_data[1])
    R = int(input_data[2])
    
    idx = 3
    railways = []
    for _ in range(F):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        railways.append((c, u, v))
        idx += 3
        
    highways = []
    for _ in range(R):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        highways.append((c, u, v))
        idx += 3
        
    railways.sort()
    highways.sort()
    
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
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    total_cost = 0
    for c, u, v in railways:
        if union(u, v):
            total_cost += c
            
    for c, u, v in highways:
        if union(u, v):
            total_cost += c
            
    print(total_cost)

if __name__ == '__main__':
    solve()