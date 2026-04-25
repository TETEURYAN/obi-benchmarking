import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    
    # Fenwick Tree (BIT)
    tree = [0] * (n + 1)
    
    def update(i, delta):
        while i <= n:
            tree[i] += delta
            i += i & (-i)
    
    def query(i):
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & (-i)
        return s
    
    # Initialize with floor values
    floors = [0] * (n + 1)
    for i in range(1, n + 1):
        val = int(data[idx]); idx += 1
        floors[i] = val
        update(i, val)
    
    out = []
    for _ in range(q):
        event = int(data[idx]); idx += 1
        if event == 0:
            k = int(data[idx]); idx += 1
            p = int(data[idx]); idx += 1
            delta = p - floors[k]
            floors[k] = p
            update(k, delta)
        else:
            k = int(data[idx]); idx += 1
            out.append(query(k))
    
    print('\n'.join(map(str, out)))

main()