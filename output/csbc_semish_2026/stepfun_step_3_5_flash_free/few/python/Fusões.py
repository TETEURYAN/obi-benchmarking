import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    parent = list(range(n+1))
    size = [1] * (n+1)
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
    out = []
    for _ in range(k):
        op = next(it)
        a = int(next(it))
        b = int(next(it))
        if op == 'F':
            union(a, b)
        else:
            out.append('S' if find(a) == find(b) else 'N')
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()