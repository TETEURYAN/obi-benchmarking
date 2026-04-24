import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
D = data[1]
c = data[2:2 + n]

ans = 0

# Contar segmentos contínuos com soma D
l = 0
s = 0
for r in range(n):
    s += c[r]
    while s > D and l <= r:
        s -= c[l]
        l += 1
    if s == D:
        ans += 1

# Contar escolhas pelas extremidades:
# prefixo até i e sufixo a partir de j, com 1 <= i < j <= N
# soma = pref[i] + (total - pref[j-1]) = D
# => pref[i] - pref[j-1] = D - total
# Como Ci > 0, prefixos são estritamente crescentes.
total = sum(c)
target = D - total

pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + c[i - 1]

j = 2
for i in range(1, n):
    need = pref[i] - target
    while j <= n and pref[j - 1] < need:
        j += 1
    if j <= n and pref[j - 1] == need:
        ans += 1

print(ans)