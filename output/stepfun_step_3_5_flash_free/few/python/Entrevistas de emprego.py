import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    mat = [next(it) for _ in range(n)]
    
    parent = list(range(n+1))
    rank = [0]*(n+1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
    
    for i in range(1, n+1):
        row = mat[i-1]
        for j in range(i+1, n+1):
            if row[j-1] == '1':
                union(i, j)
    
    e = int(next(it))
    out = []
    for _ in range(e):
        k = int(next(it))
        cand = [int(next(it)) for _ in range(k)]
        seen = set()
        ok = False
        for c in cand:
            r = find(c)
            if r in seen:
                ok = True
                break
            seen.add(r)
        out.append('S' if ok else 'N')
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()