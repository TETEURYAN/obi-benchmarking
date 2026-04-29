import sys

def main():
    input = sys.stdin.readline

    X, Y = map(int, input().split())
    N, A = map(int, input().split())

    cities = []
    for i in range(N):
        x, y = map(int, input().split())
        cities.append((x, y, i))

    limit = A // 100

    parent = list(range(N))
    rank = [0] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1

    # Conecta cidades na mesma vertical (mesmo x), ordenadas por y
    by_x = {}
    for x, y, i in cities:
        by_x.setdefault(x, []).append((y, i))

    for x in by_x:
        arr = by_x[x]
        arr.sort()
        for j in range(1, len(arr)):
            if arr[j][0] - arr[j - 1][0] <= limit:
                union(arr[j][1], arr[j - 1][1])

    # Conecta cidades na mesma horizontal (mesmo y), ordenadas por x
    by_y = {}
    for x, y, i in cities:
        by_y.setdefault(y, []).append((x, i))

    for y in by_y:
        arr = by_y[y]
        arr.sort()
        for j in range(1, len(arr)):
            if arr[j][0] - arr[j - 1][0] <= limit:
                union(arr[j][1], arr[j - 1][1])

    comps = set(find(i) for i in range(N))
    print(len(comps) - 1)

if __name__ == "__main__":
    main()
