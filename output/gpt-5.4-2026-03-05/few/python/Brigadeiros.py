import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

it = iter(data)
N = next(it)
K = next(it)
T = next(it)

P = [0] + [next(it) for _ in range(N)]
G = [0] + [next(it) for _ in range(N)]

friends = [i for i in range(1, N + 1) if G[i] == 1]

INF_NEG = -10**18

# dp[j][c] = melhor soma usando alguns primeiros pratos,
# escolhendo j posições finais para os j primeiros amigos,
# com custo total exato c (c limitado por max_cost)
max_cost = min(T, K * N)

dp = [[INF_NEG] * (max_cost + 1) for _ in range(K + 1)]
dp[0][0] = 0

for pos in range(1, N + 1):
    up = min(pos, K)
    for j in range(up, 0, -1):
        cost_add = abs(friends[j - 1] - pos)
        if cost_add > max_cost:
            continue
        prev = dp[j - 1]
        cur = dp[j]
        val = P[pos]
        limit = max_cost - cost_add
        for c in range(limit, -1, -1):
            if prev[c] != INF_NEG:
                nv = prev[c] + val
                nc = c + cost_add
                if nv > cur[nc]:
                    cur[nc] = nv

ans = 0
for c in range(max_cost + 1):
    if c <= T and dp[K][c] > ans:
        ans = dp[K][c]

print(ans)