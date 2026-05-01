
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    teste = 1
    
    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
            if n == 0:
                break
            
            m = int(next(iterator))
            
            edges = []
            for _ in range(m):
                u = int(next(iterator))
                v = int(next(iterator))
                w = int(next(iterator))
                if u > v:
                    u, v = v, u
                edges.append((w, u, v))
            
            edges.sort()
            
            parent = list(range(n + 1))
            rank = [0] * (n + 1)
            
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
            
            mst = []
            for w, u, v in edges:
                if union(u, v):
                    mst.append((u, v))
            
            mst.sort()
            
            print(f"Teste {teste}")
            for u, v in mst:
                print(f"{u} {v}")
            print()
            
            teste += 1
            
        except StopIteration:
            break

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    solve()
