import sys

def main():
    input = sys.stdin.readline

    X, Y = map(int, input().split())
    N, A = map(int, input().split())

    cities = [tuple(map(int, input().split())) for _ in range(N)]

    if A < 100:
        print(N - 1)
        return

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

    by_x = {}
    by_y = {}

    for i, (x, y) in enumerate(cities):
        by_x.setdefault(x, []).append((y, i))
        by_y.setdefault(y, []).append((x, i))

    for x, arr in by_x.items():
        arr.sort()
        l = 0
        for r in range(1, len(arr)):
            while arr[r][0] - arr[l][0] > limit:
                l += 1
            if l < r:
                union(arr[l][1], arr[r][1])

    for y, arr in by_y.items():
        arr.sort()
        l = 0
        for r in range(1, len(arr)):
            while arr[r][0] - arr[l][0] > limit:
                l += 1
            if l < r:
                union(arr[l][1], arr[r][1])

    comps = set(find(i) for i in range(N))
    print(len(comps) - 1)

if __name__ == "__main__":
    main()
