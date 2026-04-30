
import sys

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    result = []
    i = 0
    e = 0
    while e < n-1 and i < len(edges):
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v))
            union(parent, rank, x, y)
    return result

def main():
    input_lines = [line.strip() for line in sys.stdin if line.strip()]
    idx = 0
    teste_num = 1
    while idx < len(input_lines):
        N, M = map(int, input_lines[idx].split())
        if N == 0:
            break
        edges = []
        idx += 1
        for _ in range(M):
            X, Y, Z = map(int, input_lines[idx].split())
            edges.append((X, Y, Z))
            idx += 1
        result = kruskal(N, edges)
        print(f"Teste {teste_num}")
        for u, v in result:
            if u > v:
                u, v = v, u
            print(u, v)
        print()
        teste_num += 1

if __name__ == "__main__":
    main()
