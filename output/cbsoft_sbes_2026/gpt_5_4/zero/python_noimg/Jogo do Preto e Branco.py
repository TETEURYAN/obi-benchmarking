import sys

def main():
    input = sys.stdin.readline
    L, C = map(int, input().split())
    P = int(input())
    
    black = [[False] * C for _ in range(L)]
    for _ in range(P):
        x, y = map(int, input().split())
        black[x - 1][y - 1] = True

    allmask = (1 << C) - 1

    valid_masks = []
    for m in range(1 << C):
        if (m & (m << 1)) == 0:
            valid_masks.append(m)

    allowed = []
    popcount = {}
    for i in range(L):
        row_black = 0
        up_black = 0
        down_black = 0
        for j in range(C):
            if black[i][j]:
                row_black |= 1 << j
            if i > 0 and black[i - 1][j]:
                up_black |= 1 << j
            if i + 1 < L and black[i + 1][j]:
                down_black |= 1 << j

        can_have_black_neighbor = ((row_black << 1) | (row_black >> 1) | up_black | down_black) & allmask
        row_allowed = []
        for m in valid_masks:
            if (m & row_black) == 0 and (m & ~can_have_black_neighbor) == 0:
                row_allowed.append(m)
                popcount[m] = m.bit_count()
        allowed.append(row_allowed)

    dp = {0: 0}
    for i in range(L):
        ndp = {}
        for prev_mask, val in dp.items():
            for m in allowed[i]:
                if (m & prev_mask) == 0:
                    nv = val + popcount[m]
                    if nv > ndp.get(m, -1):
                        ndp[m] = nv
        dp = ndp

    print(max(dp.values(), default=0))

if __name__ == "__main__":
    main()
