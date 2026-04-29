import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    P = int(next(it))

    black = [[False] * C for _ in range(L)]
    for _ in range(P):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        black[x][y] = True

    row_black = [0] * L
    row_allowed = [0] * L

    for r in range(L):
        bmask = 0
        for c in range(C):
            if black[r][c]:
                bmask |= 1 << c
        row_black[r] = bmask

    for r in range(L):
        amask = 0
        for c in range(C):
            if black[r][c]:
                continue
            ok = False
            if r > 0 and black[r - 1][c]:
                ok = True
            if r + 1 < L and black[r + 1][c]:
                ok = True
            if c > 0 and black[r][c - 1]:
                ok = True
            if c + 1 < C and black[r][c + 1]:
                ok = True
            if ok:
                amask |= 1 << c
        row_allowed[r] = amask

    valid_masks = []
    for r in range(L):
        masks = []
        allowed = row_allowed[r]
        for m in range(1 << C):
            if (m & ~allowed) == 0 and (m & (m << 1)) == 0:
                masks.append(m)
        valid_masks.append(masks)

    popcount = [0] * (1 << C)
    for i in range(1, 1 << C):
        popcount[i] = popcount[i >> 1] + (i & 1)

    NEG = -10**9
    dp_prev = {0: 0}

    for r in range(L):
        dp_cur = {}
        for pmask, val in dp_prev.items():
            for mask in valid_masks[r]:
                if mask & pmask:
                    continue
                nv = val + popcount[mask]
                if nv > dp_cur.get(mask, NEG):
                    dp_cur[mask] = nv
        dp_prev = dp_cur

    print(max(dp_prev.values(), default=0))

if __name__ == "__main__":
    main()
