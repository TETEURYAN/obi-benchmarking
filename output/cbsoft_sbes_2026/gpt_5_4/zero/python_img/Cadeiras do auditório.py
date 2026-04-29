import sys

def decompose_swaps(perm):
    n = len(perm) - 1
    visited = [False] * (n + 1)
    ops = []
    for i in range(1, n + 1):
        if not visited[i]:
            cyc = []
            x = i
            while not visited[x]:
                visited[x] = True
                cyc.append(x)
                x = perm[x]
            m = len(cyc)
            if m > 1:
                a1 = cyc[0]
                for k in range(m - 1, 0, -1):
                    ops.append((a1, cyc[k]))
    return ops

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))

    row_perm = [0] * (L + 1)
    col_perm = [0] * (C + 1)

    first = int(next(it))
    row_perm[1] = (first - 1) // C + 1
    col_perm[1] = (first - 1) % C + 1

    for j in range(2, C + 1):
        x = int(next(it))
        col_perm[j] = (x - 1) % C + 1

    for i in range(2, L + 1):
        x = int(next(it))
        row_perm[i] = (x - 1) // C + 1
        for _ in range(C - 1):
            next(it)

    row_ops = decompose_swaps(row_perm)
    col_ops = decompose_swaps(col_perm)

    out = []
    out.append(str(len(row_ops) + len(col_ops)))
    for a, b in row_ops:
        out.append(f"L {a} {b}")
    for a, b in col_ops:
        out.append(f"C {a} {b}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
