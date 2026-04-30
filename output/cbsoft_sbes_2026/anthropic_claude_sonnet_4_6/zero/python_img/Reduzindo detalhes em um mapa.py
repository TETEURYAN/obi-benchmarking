import sys
input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append((c, u, v))
    edges.sort()
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total = 0
    for c, u, v in edges:
        if union(parent, rank, u, v):
            total += c
    print(total)

main()