import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
idx = 1

# Faces in input order:
# 0:A, 1:B, 2:C, 3:D, 4:E, 5:F
# Opposite pairs according to the standard figure used in the problem:
# (A,F), (B,D), (C,E)
opp = [5, 3, 4, 1, 2, 0]

# For each possible top value t (1..6), best side value achievable on this die
best_side = [[0] * 7 for _ in range(n)]

for i in range(n):
    vals = data[idx:idx+6]
    idx += 6

    pos = [0] * 7
    for p, v in enumerate(vals):
        pos[v] = p

    for top in range(1, 7):
        ptop = pos[top]
        pbot = opp[ptop]
        bottom = vals[pbot]

        mx = 0
        for v in vals:
            if v != top and v != bottom and v > mx:
                mx = v
        best_side[i][top] = mx

dp = [0] * 7
for top in range(1, 7):
    dp[top] = best_side[0][top]

for i in range(1, n):
    ndp = [0] * 7
    cur = best_side[i]
    for prev_top in range(1, 7):
        val = dp[prev_top]
        if val == 0 and n > 0:
            pass
        bottom = prev_top
        for top in range(1, 7):
            # On die i, if bottom is fixed, top is uniquely determined
            # We invert using the same precomputed relation from values.
            # Since values are 1..6 distinct, top can only be the opposite of bottom.
            # So only one transition is valid.
            pass

    # Build direct transition using opposite values on this die
    vals = data[1 + 6*i:1 + 6*i + 6]
    pos = [0] * 7
    for p, v in enumerate(vals):
        pos[v] = p

    for prev_top in range(1, 7):
        pbot = pos[prev_top]
        top = vals[opp[pbot]]
        cand = dp[prev_top] + cur[top]
        if cand > ndp[top]:
            ndp[top] = cand

    dp = ndp

print(max(dp[1:]))