import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
    
    out = []
    for _ in range(k):
        op = data[idx]; idx += 1
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        if op == 'F':
            union(a, b)
        else:
            if find(a) == find(b):
                out.append('S')
            else:
                out.append('N')
    
    print('\n'.join(out))

main()