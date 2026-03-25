import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    arr = [0] * (N + 1)
    for i in range(1, N + 1):
        arr[i] = int(data[idx]); idx += 1
    
    # BIT (Fenwick Tree)
    bit = [0] * (N + 2)
    
    def update(pos, delta):
        while pos <= N:
            bit[pos] += delta
            pos += pos & -pos
    
    def query(pos):
        s = 0
        while pos > 0:
            s += bit[pos]
            pos -= pos & -pos
        return s
    
    # inicializa BIT
    for i in range(1, N + 1):
        update(i, arr[i])
    
    out_lines = []
    for _ in range(Q):
        t = int(data[idx]); idx += 1
        if t == 0:
            K = int(data[idx]); idx += 1
            P = int(data[idx]); idx += 1
            delta = P - arr[K]
            arr[K] = P
            update(K, delta)
        else:  # t == 1
            K = int(data[idx]); idx += 1
            out_lines.append(str(query(K)))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()