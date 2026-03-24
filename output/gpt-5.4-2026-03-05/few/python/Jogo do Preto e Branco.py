import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

L, C = data[0], data[1]
P = data[2]

black = [[False] * C for _ in range(L)]
idx = 3
for _ in range(P):
    x = data[idx] - 1
    y = data[idx + 1] - 1
    black[x][y] = True
    idx += 2

eligible = [0] * L
blocked = [0] * L

for r in range(L):
    em = 0
    bm = 0
    for c in range(C):
        if black[r][c]:
            bm |= 1 << c
        else:
            ok = False
            if r > 0 and black[r - 1][c]:
                ok = True
            elif r + 1 < L and black[r + 1][c]:
                ok = True
            elif c > 0 and black[r][c - 1]:
                ok = True
            elif c + 1 < C and black[r][c + 1]:
                ok = True
            if ok:
                em |= 1 << c
    eligible[r] = em
    blocked[r] = bm

valid_masks = []
for r in range(L):
    row_valid = []
    em = eligible[r]
    bm = blocked[r]
    for mask in range(1 << C):
        if mask & bm:
            continue
        if mask & ~em:
            continue
        if mask & (mask << 1):
            continue
        row_valid.append((mask, mask.bit_count()))
    valid_masks.append(row_valid)

dp = {0: 0}
for r in range(L):
    ndp = {}
    for prev_mask, val in dp.items():
        for mask, cnt in valid_masks[r]:
            if mask & prev_mask:
                continue
            nv = val + cnt
            cur = ndp.get(mask)
            if cur is None or nv > cur:
                ndp[mask] = nv
    dp = ndp

print(max(dp.values(), default=0))