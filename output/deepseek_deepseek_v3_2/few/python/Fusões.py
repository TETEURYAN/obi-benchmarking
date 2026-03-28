import sys
sys.setrecursionlimit(200000)

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, size):
    ra = find(a, parent)
    rb = find(b, parent)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    
    out_lines = []
    for _ in range(K):
        op = data[idx]; idx += 1
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        if op == 'F':
            union(a, b, parent, size)
        else:  # op == 'C'
            if find(a, parent) == find(b, parent):
                out_lines.append('S')
            else:
                out_lines.append('N')
    
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()