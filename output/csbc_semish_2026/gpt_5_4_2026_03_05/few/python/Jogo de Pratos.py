import sys

MOD = 10**9 + 7

data = list(map(int, sys.stdin.read().split()))
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

# Best spell repeated K times:
# maximize a*x+b for all x>=1.
# If any spell has a>1, best strategy is to use one spell maximizing (a,b) lexicographically by a then b, repeated K times.
# If all a=1, use spell with maximum b, repeated K times.
best_spell_a = 1
best_spell_b = 0
for a, b in zip(spell_a, spell_b):
    if a > best_spell_a or (a == best_spell_a and b > best_spell_b):
        best_spell_a = a
        best_spell_b = b

# Sort meals by threshold t = b/(a-1) for a>1; a=1 meals go last.
# For maximizing final value for any x, optimal order is by increasing threshold.
meals = list(zip(meal_a, meal_b))

def cmp_key(effect):
    a, b = effect
    if a == 1:
        return (1, 0, 0)
    return (0, b, a - 1)

# Need exact comparison by cross multiplication, so use custom sort via transformed comparator not enough.
# We'll sort with Python's stable sort using fractions through rich comparison avoided;
# instead use key for a==1 separation and then sort a>1 by b/(a-1) using cross products via merge sort.

gt1 = [(a, b) for a, b in meals if a > 1]
eq1 = [(a, b) for a, b in meals if a == 1]

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n >> 1
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        a1, b1 = left[i]
        a2, b2 = right[j]
        if b1 * (a2 - 1) <= b2 * (a1 - 1):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res

gt1 = merge_sort(gt1)
meals_sorted = gt1 + eq1

# Compose all meals: y -> A_meal * y + B_meal (mod MOD)
A_meal = 1
B_meal = 0
for a, b in meals_sorted:
    A_meal = (a % MOD) * A_meal % MOD
    B_meal = ((a % MOD) * B_meal + b) % MOD

# Spell composition repeated K times
sa = best_spell_a
sb = best_spell_b

if K == 0:
    A_spell = 1
    B_spell = 0
elif sa == 1:
    A_spell = 1
    B_spell = (sb % MOD) * (K % MOD) % MOD
else:
    A_spell = pow(sa % MOD, K, MOD)
    inv = pow((sa - 1) % MOD, MOD - 2, MOD)
    geom = (A_spell - 1) % MOD * inv % MOD
    B_spell = (sb % MOD) * geom % MOD

# Final composition: meals(spells(x)) = A_meal*(A_spell*x + B_spell) + B_meal
FA = A_meal * A_spell % MOD
FB = (A_meal * B_spell + B_meal) % MOD

out = []
for x in queries:
    out.append(str((FA * (x % MOD) + FB) % MOD))

sys.stdout.write("\n".join(out))