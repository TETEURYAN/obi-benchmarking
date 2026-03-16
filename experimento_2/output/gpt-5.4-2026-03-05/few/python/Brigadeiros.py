import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k, T = data[0], data[1], data[2]
p = [0] + data[3:3 + n]
g = [0] + data[3 + n:3 + 2 * n]

friends = []
for i in range(1, n + 1):
    if g[i] == 1:
        friends.append(i)

INF = -10**18

dp = [[INF] * (n + 1) for _ in range(k + 1)]
for j in range(n + 1):
    dp[0][j] = 0

for i in range(1, k + 1):
    s = friends[i - 1]
    for j in range(i, n - (k - i) + 1):
        best = INF
        prev = dp[i - 1]
        for x in range(i - 1, j):
            val = prev[x]
            if val != INF:
                cost = abs(s - j)
                cand = val - cost
                if cand > best:
                    best = cand
        if best != INF:
            dp[i][j] = best + p[j]

ans = 0
for j in range(k, n + 1):
    val = dp[k][j]
    if val >= -10**17 and val + T > ans:
        ans = val + T

best_sum = 0
for j in range(k, n + 1):
    val = dp[k][j]
    if val >= -10**17:
        total_brig = val
        # val = sum - cost, so feasible iff cost <= T <=> total_brig >= sum - T not directly useful
        # recover by checking total_brig + T = sum + (T - cost)
        # need max sum among states with cost <= T
        pass

dp2 = [[INF] * (n + 1) for _ in range(k + 1)]
for j in range(n + 1):
    dp2[0][j] = 0

for i in range(1, k + 1):
    s = friends[i - 1]
    for j in range(i, n - (k - i) + 1):
        best = INF
        prev = dp2[i - 1]
        for x in range(i - 1, j):
            val = prev[x]
            if val != INF:
                cost = abs(s - j)
                cand = val
                if cand > best:
                    best = cand
        if best != INF:
            dp2[i][j] = best + p[j]

maxT = min(T, k * n)
reach = [[-1] * (maxT + 1) for _ in range(k + 1)]
reach[0][0] = 0

for i in range(1, k + 1):
    s = friends[i - 1]
    for t in range(maxT + 1):
        best_pos = -1
        for x in range(i - 1, n + 1):
            if reach[i - 1][t] >= x:
                best_pos = x
        for j in range(i, n - (k - i) + 1):
            c = abs(s - j)
            if c <= t and reach[i - 1][t - c] >= j - 1:
                if j > reach[i][t]:
                    reach[i][t] = j

dpv = [[INF] * (maxT + 1) for _ in range(k + 1)]
states = [[INF] * (n + 1) for _ in range(k + 1)]
for j in range(n + 1):
    states[0][j] = 0

for i in range(1, k + 1):
    s = friends[i - 1]
    ndp = [[INF] * (n + 1) for _ in range(maxT + 1)]
    for used in range(maxT + 1):
        for j in range(i, n - (k - i) + 1):
            c = abs(s - j)
            if c > used:
                continue
            best = INF
            for x in range(i - 1, j):
                prev = ndp[used - c][x] if False else None
            # not used

# O(N^3) DP by exact cost, acceptable since N<=300 and effective cost cap <= 90000 may be too large.
# Use min-cost formulation with Lagrangian and exploit small N:
# Since each move cost is at most N and K<=N, total necessary cost to realize any ordering is <= N^2/2.
# If T >= N*N, all assignments are feasible.
max_possible_cost = n * n
if T >= max_possible_cost:
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    for j in range(n + 1):
        dp[0][j] = 0
    for i in range(1, k + 1):
        for j in range(i, n - (k - i) + 1):
            best = INF
            for x in range(i - 1, j):
                if dp[i - 1][x] > best:
                    best = dp[i - 1][x]
            dp[i][j] = best + p[j]
    print(max(dp[k][j] for j in range(k, n + 1)))
    sys.exit()

C = min(max_possible_cost, T)

dp = [[INF] * (C + 1) for _ in range(n + 1)]
dp[0][0] = 0

for idx_f, s in enumerate(friends, 1):
    ndp = [[INF] * (C + 1) for _ in range(n + 1)]
    prefix = [[INF] * (C + 1) for _ in range(n + 1)]
    for pos in range(n + 1):
        row = dp[pos]
        prow = prefix[pos]
        if pos == 0:
            for c in range(C + 1):
                prow[c] = row[c]
        else:
            prevp = prefix[pos - 1]
            for c in range(C + 1):
                a = prevp[c]
                b = row[c]
                prow[c] = a if a > b else b
    for j in range(idx_f, n - (k - idx_f) + 1):
        move = abs(s - j)
        if move > C:
            continue
        best_prev = prefix[j - 1]
        out = ndp[j]
        pj = p[j]
        for c in range(move, C + 1):
            val = best_prev[c - move]
            if val != INF:
                out[c] = val + pj
    dp = ndp

ans = 0
for j in range(k, n + 1):
    row = dp[j]
    for c in range(C + 1):
        if row[c] > ans:
            ans = row[c]

print(ans)