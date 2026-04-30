import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    test_case = 1
    
    while True:
        try:
            n_str = next(iterator)
            m_str = next(iterator)
        except StopIteration:
            break
            
        n = int(n_str)
        m = int(m_str)
        
        if n == 0:
            break
            
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            if u > v:
                u, v = v, u
            edges.append((w, u, v))
            
        edges.sort(key=lambda x: (x[0], x[1], x[2]))
        
        dsu = DSU(n)
        mst = []
        
        for w, u, v in edges:
            if dsu.union(u, v):
                mst.append((u, v))
                
        mst.sort()
        
        print(f"Teste {test_case}")
        for u, v in mst:
            print(f"{u} {v}")
        print()
        
        test_case += 1

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    solve()