
import sys

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))  # 1-based indexing
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True

def main():
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    index = 0
    test_case = 1
    while index < len(input_lines):
        N, M = map(int, input_lines[index].split())
        index += 1
        if N == 0 and M == 0:
            break
        edges = []
        for _ in range(M):
            X, Y, Z = map(int, input_lines[index].split())
            edges.append((Z, X, Y))
            index += 1
        edges.sort()
        uf = UnionFind(N)
        result = []
        for Z, X, Y in edges:
            if uf.union(X, Y):
                result.append((X, Y))
        print(f"Teste {test_case}")
        for X, Y in result:
            print(f"{X} {Y}")
        print()
        test_case += 1

if __name__ == "__main__":
    main()
