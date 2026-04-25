import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    test_case = 1
    
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
            
        parent = list(range(7))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        degree = [0] * 7
        for _ in range(n):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            degree[u] += 1
            degree[v] += 1
            union(u, v)
            
        odd_count = sum(1 for d in degree if d % 2 != 0)
        possible = (odd_count == 0 or odd_count == 2)
        
        if possible:
            first_component = -1
            for i in range(7):
                if degree[i] > 0:
                    if first_component == -1:
                        first_component = find(i)
                    elif find(i) != first_component:
                        possible = False
                        break
                        
        print(f"Teste {test_case}")
        if possible:
            print("sim")
        else:
            print("nao")
        print()
            
        test_case += 1

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    solve()