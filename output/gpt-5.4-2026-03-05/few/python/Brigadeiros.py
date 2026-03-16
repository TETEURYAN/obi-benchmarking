import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n, k, T = data[0], data[1], data[2]
p = data[3:3+n]
g = data[3+n:3+2*n]

friends = [i + 1 for i, x in enumerate(g) if x == 1]

INF_NEG = -10**18

# dp[j][c] = melhor soma usando alguns primeiros amigos,
# colocando o último amigo na posição j, com custo total c
# custo = soma dos deslocamentos absolutos
# Como uma troca entre vizinhos altera a soma dos deslocamentos em 1
# e podemos sempre realizar exatamente esse mínimo sem conflitos
# para um conjunto final ordenado, basta exigir custo <= T.

max_cost = min(T, n * n)

prev = [[INF_NEG] * (max_cost + 1) for _ in range(n + 1)]

f0 = friends[0]
for j in range(1, n + 1):
    c = abs(f0 - j)
    if c <= max_cost:
        prev[j][c] = p[j - 1]

for idx in range(1, k):
    fi = friends[idx]
    curr = [[INF_NEG] * (max_cost + 1) for _ in range(n + 1)]

    # prefix best over previous positions < j
    # for each cost
    best = [INF_NEG] * (max_cost + 1)

    for j in range(1, n + 1):
        row_prev = prev[j - 1]
        for c in range(max_cost + 1):
            if row_prev[c] > best[c]:
                best[c] = row_prev[c]

        move_cost = abs(fi - j)
        if move_cost > max_cost:
            continue

        val = p[j - 1]
        limit = max_cost - move_cost
        row_curr = curr[j]
        for c in range(limit + 1):
            b = best[c]
            if b != INF_NEG:
                row_curr[c + move_cost] = b + val

    prev = curr

ans = 0
for j in range(1, n + 1):
    row = prev[j]
    best_row = max(row)
    if best_row > ans:
        ans = best_row

print(ans)