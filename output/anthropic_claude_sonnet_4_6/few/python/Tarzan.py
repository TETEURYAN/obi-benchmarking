import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    trees = []
    for _ in range(n):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        trees.append((x, y))
    
    parent = list(range(n))
    
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    
    d2 = d * d
    for i in range(n):
        for j in range(i+1, n):
            dx = trees[i][0] - trees[j][0]
            dy = trees[i][1] - trees[j][1]
            if dx*dx + dy*dy <= d2:
                union(i, j)
    
    root = find(0)
    for i in range(1, n):
        if find(i) != root:
            print('N')
            return
    print('S')

main()