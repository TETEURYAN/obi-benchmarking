import sys

def decompose_swaps(p):
    n = len(p) - 1
    vis = [False] * (n + 1)
    ops = []
    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            cyc = []
            while not vis[cur]:
                vis[cur] = True
                cyc.append(cur)
                cur = p[cur]
            if len(cyc) > 1:
                a0 = cyc[0]
                for k in range(len(cyc) - 1, 0, -1):
                    ops.append((a0, cyc[k]))
    return ops

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))

    row_map = [0] * (L + 1)   # current row i came from original row row_map[i]
    col_map = [0] * (C + 1)   # current col j came from original col col_map[j]

    for i in range(1, L + 1):
        first = int(next(it))
        r0 = (first - 1) // C + 1
        c0 = (first - 1) % C + 1
        row_map[i] = r0
        col_map[1] = c0 if i == 1 else col_map[1]

        for j in range(2, C + 1):
            x = int(next(it))
            if i == 1:
                col_map[j] = (x - 1) % C + 1

    row_inv = [0] * (L + 1)
    col_inv = [0] * (C + 1)
    for i in range(1, L + 1):
        row_inv[row_map[i]] = i
    for j in range(1, C + 1):
        col_inv[col_map[j]] = j

    ops = []
    for a, b in decompose_swaps(row_inv):
        ops.append(f"L {a} {b}")
    for a, b in decompose_swaps(col_inv):
        ops.append(f"C {a} {b}")

    sys.stdout.write(str(len(ops)) + "\n")
    if ops:
        sys.stdout.write("\n".join(ops))

if __name__ == "__main__":
    main()
