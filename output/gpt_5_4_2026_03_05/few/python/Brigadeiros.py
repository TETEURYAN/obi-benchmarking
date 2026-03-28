import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = iter(data)
N = next(it)
K = next(it)
T = next(it)

P = [next(it) for _ in range(N)]
G = [next(it) for _ in range(N)]

friends = []
for i, x in enumerate(G, 1):
    if x == 1:
        friends.append(i)

INF_NEG = -10**18

dp = [[INF_NEG] * (T if T < N * N else N * N) for _ in range(1)]
max_cost_cap = N * N

dp = [INF_NEG] * (max_cost_cap + 1)
dp[0] = 0

for a, pos in enumerate(friends, 1):
    ndp = [INF_NEG] * (max_cost_cap + 1)
    min_j = a
    max_j = N - (K - a)
    for j in range(min_j, max_j + 1):
        cost = abs(pos - j)
        val = P[j - 1]
        for c in range(cost, max_cost_cap + 1):
            prev = dp[c - cost]
            if prev != INF_NEG:
                cand = prev + val
                if cand > ndp[c]:
                    ndp[c] = cand
    dp = ndp

limit = min(T, max_cost_cap)
ans = 0
for c in range(limit + 1):
    if dp[c] > ans:
        ans = dp[c]

print(ans)