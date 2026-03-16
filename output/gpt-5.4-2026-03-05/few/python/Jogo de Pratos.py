import sys

MOD = 10**9 + 7

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

it = iter(data)
N = next(it)
M = next(it)
K = next(it)

spell_a = [next(it) for _ in range(N)]
spell_b = [next(it) for _ in range(N)]
meal_a = [next(it) for _ in range(M)]
meal_b = [next(it) for _ in range(M)]
Q = next(it)
queries = [next(it) for _ in range(Q)]

# Best spell for repeated use:
# maximize a*x+b for all x>=1
# If a1>a2 then spell1 better for all sufficiently large x, and with x>=1
# compare by a+b.
best_sa = spell_a[0]
best_sb = spell_b[0]
best_sum = best_sa + best_sb
for i in range(1, N):
    s = spell_a[i] + spell_b[i]
    if s > best_sum or (s == best_sum and spell_a[i] > best_sa):
        best_sa = spell_a[i]
        best_sb = spell_b[i]
        best_sum = s

# Meals: sort by comparator:
# f before g iff (a_f-1)*b_g >= (a_g-1)*b_f
meals = list(zip(meal_a, meal_b))
meals.sort(key=lambda x: 0)  # placeholder to keep stable if needed

from functools import cmp_to_key

def cmp(u, v):
    au, bu = u
    av, bv = v
    left = (au - 1) * bv
    right = (av - 1) * bu
    if left > right:
        return -1
    if left < right:
        return 1
    return 0

meals.sort(key=cmp_to_key(cmp))

# Compose all meals into F(x)=A*x+B
mealA_mod = 1
mealB_mod = 0
for a, b in meals:
    mealB_mod = (a % MOD) * mealB_mod + b
    mealB_mod %= MOD
    mealA_mod = mealA_mod * (a % MOD) % MOD

# For deciding optimal number of spell uses t in [0,K]:
# final after t spells then all meals:
# A_meal * S_t(x) + B_meal
# so maximize S_t(x) only.
#
# Repeating best spell (a,b):
# if a=1: x + t*b
# else: a^t*x + b*(a^t-1)/(a-1)
#
# Need choose t maximizing exact integer value for each x.
# Since a+b>1, repeated best spell is nondecreasing in t for x>=1:
# S_{t+1}-S_t = (a-1)S_t + b >= (a-1)*1 + b = a+b-1 > 0
# Therefore optimal t = K always.

sa = best_sa
sb = best_sb

if sa == 1:
    add_mod = (K % MOD) * (sb % MOD) % MOD
    out = []
    for x in queries:
        s_mod = (x % MOD + add_mod) % MOD
        ans = (mealA_mod * s_mod + mealB_mod) % MOD
        out.append(str(ans))
else:
    pow_a = pow(sa, K, MOD)
    inv = pow(sa - 1, MOD - 2, MOD)
    geom = (pow_a - 1) * inv % MOD
    const_mod = (sb % MOD) * geom % MOD
    out = []
    for x in queries:
        s_mod = (pow_a * (x % MOD) + const_mod) % MOD
        ans = (mealA_mod * s_mod + mealB_mod) % MOD
        out.append(str(ans))

sys.stdout.write("\n".join(out))