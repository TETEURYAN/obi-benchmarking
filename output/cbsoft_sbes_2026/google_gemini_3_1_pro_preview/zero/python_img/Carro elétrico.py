
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    X = int(input_data[0])
    Y = int(input_data[1])
    N = int(input_data[2])
    A = int(input_data[3])
    
    cities = []
    idx = 4
    for _ in range(N):
        cities.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    parent = list(range(N))
    components = N
    
    for i in range(N):
        xi, yi = cities[i]
        for j in range(i + 1, N):
            xj, yj = cities[j]
            if 100 * (abs(xi - xj) + abs(yi - yj)) <= A:
                root_i = i
                while parent[root_i] != root_i:
                    parent[root_i] = parent[parent[root_i]]
                    root_i = parent[root_i]
                
                root_j = j
                while parent[root_j] != root_j:
                    parent[root_j] = parent[parent[root_j]]
                    root_j = parent[root_j]
                
                if root_i != root_j:
                    parent[root_i] = root_j
                    components -= 1
                    
    print(components - 1)

if __name__ == '__main__':
    solve()
