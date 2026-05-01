import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        p, q, u = map(int, input().split())
        edges.append((u, p, q))

    edges.sort()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    ans = 0

    for w, a, b in edges:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            ans += w
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

    print(ans)

if __name__ == "__main__":
    main()