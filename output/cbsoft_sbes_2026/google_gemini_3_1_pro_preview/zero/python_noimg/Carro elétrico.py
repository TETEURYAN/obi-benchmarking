import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[2])
    A = int(input_data[3])
    
    parent = list(range(N))
    rank = [0] * N
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i
        
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            return True
        return False

    cities_x = [0] * N
    cities_y = [0] * N
    idx = 4
    for i in range(N):
        cities_x[i] = int(input_data[idx])
        cities_y[i] = int(input_data[idx+1])
        idx += 2
        
    components = N
    max_dist = A // 100
    
    for i in range(N):
        xi = cities_x[i]
        yi = cities_y[i]
        for j in range(i + 1, N):
            if abs(xi - cities_x[j]) + abs(yi - cities_y[j]) <= max_dist:
                if union(i, j):
                    components -= 1
                    
    print(components - 1)

if __name__ == '__main__':
    solve()