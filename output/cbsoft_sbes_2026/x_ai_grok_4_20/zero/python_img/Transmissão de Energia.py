
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

def is_connected(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    components = n
    for u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            union(parent, rank, x, y)
            components -= 1
    return components == 1

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    test = 1
    while True:
        E = int(data[index])
        L = int(data[index + 1])
        index += 2
        if E == 0 and L == 0:
            break
        edges = []
        for _ in range(L):
            X = int(data[index])
            Y = int(data[index + 1])
            index += 2
            edges.append((X, Y))
        state = "normal" if is_connected(E, edges) else "falha"
        print(f"Teste {test}")
        print(state)
        print()
        test += 1

if __name__ == "__main__":
    main()
