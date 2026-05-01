
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_num = 1
    
    while True:
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        if N == 0:
            break
        
        edges = []
        for _ in range(M):
            X = int(data[index])
            Y = int(data[index + 1])
            Z = int(data[index + 2])
            index += 3
            if X > Y:
                X, Y = Y, X
            edges.append((Z, X, Y))
        
        edges.sort()
        
        uf = UnionFind(N)
        mst_edges = []
        
        for cost, u, v in edges:
            if uf.union(u, v):
                mst_edges.append((u, v))
            if len(mst_edges) == N - 1:
                break
        
        print(f"Teste {test_num}")
        for u, v in mst_edges:
            print(u, v)
        print()
        
        test_num += 1

if __name__ == "__main__":
    main()
