import sys

MOD = 10**9 + 7

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

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
# maximize a*x+b for all x>=1.
# If any spell has a>1, best repeated spell is one with maximum a, and among them maximum b.
# Otherwise all a=1, best is maximum b.
max_a_spell = max(spell_a)
if max_a_spell > 1:
    best_b_spell = -1
    for a, b in zip(spell_a, spell_b):
        if a == max_a_spell and b > best_b_spell:
            best_b_spell = b
    sa = max_a_spell
    sb = best_b_spell
else:
    sa = 1
    sb = max(spell_b)

# Meals ordering:
# sort by comparator (a1,b1) before (a2,b2) iff b1*(a2-1) <= b2*(a1-1)
meals = list(zip(meal_a, meal_b))
meals.sort(key=lambda x: 0)  # placeholder to keep stable object type

from functools import cmp_to_key

def meal_cmp(x, y):
    ax, bx = x
    ay, by = y
    lhs = bx * (ay - 1)
    rhs = by * (ax - 1)
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    return 0

meals.sort(key=cmp_to_key(meal_cmp))

A_meals_mod = 1
B_meals_mod = 0
for a, b in meals:
    A_meals_mod = (A_meals_mod * (a % MOD)) % MOD
    B_meals_mod = (B_meals_mod * (a % MOD) + b) % MOD

# Threshold to compare spell usage count.
# For t spells then all meals:
# value = A_meals * (sa^t * x + sb * (sa^t-1)/(sa-1) if sa>1 else x+t*sb) + B_meals
# Since A_meals>0, B_meals constant, maximize pre-meal value.
# If sa>1 and sb>=0, always use K spells.
# If sa=1, use K spells iff sb>0, else any t (sb=0 impossible by constraints for all spells? still handle).
# Constraints guarantee a+b>1, so if sa=1 then sb>0.
if sa > 1:
    pow_sa_k_mod = pow(sa % MOD, K, MOD)
    inv_sa_minus_1 = pow((sa - 1) % MOD, MOD - 2, MOD)
    geom_k_mod = (pow_sa_k_mod - 1) % MOD * inv_sa_minus_1 % MOD

    out = []
    for x in queries:
        pre = (pow_sa_k_mod * (x % MOD) + (sb % MOD) * geom_k_mod) % MOD
        ans = (A_meals_mod * pre + B_meals_mod) % MOD
        out.append(str(ans))
else:
    # sa == 1, sb > 0
    add_k_mod = (K % MOD) * (sb % MOD) % MOD
    out = []
    for x in queries:
        pre = (x % MOD + add_k_mod) % MOD
        ans = (A_meals_mod * pre + B_meals_mod) % MOD
        out.append(str(ans))

sys.stdout.write("\n".join(out))