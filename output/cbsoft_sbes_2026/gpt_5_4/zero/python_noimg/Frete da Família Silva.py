import sys

sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()
    parent = list(range(N))
    size = [1] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    components = N

    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        total += w
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        components -= 1
        if components == 1:
            break

    print(total)

if __name__ == "__main__":
    main()
