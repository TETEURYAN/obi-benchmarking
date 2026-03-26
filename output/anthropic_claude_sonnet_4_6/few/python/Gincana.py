import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    parent = list(range(n + 1))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    
    for _ in range(m):
        i = int(data[idx]); idx += 1
        j = int(data[idx]); idx += 1
        union(i, j)
    
    roots = set()
    for i in range(1, n + 1):
        roots.add(find(i))
    
    print(len(roots))

main()