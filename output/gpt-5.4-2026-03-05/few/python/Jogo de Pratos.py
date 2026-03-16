import sys

MOD = 10**9 + 7

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)

    N = next(it)
    M = next(it)
    K = next(it)

    sa = [next(it) for _ in range(N)]
    sb = [next(it) for _ in range(N)]
    ma = [next(it) for _ in range(M)]
    mb = [next(it) for _ in range(M)]

    Q = next(it)
    xs = [next(it) for _ in range(Q)]

    # Best spell:
    # For x >= 1, maximizing a*x+b among spells is equivalent to maximizing (a+b),
    # because a*x+b = (a+b) + a*(x-1), and if s1=a1+b1 > s2=a2+b2 then
    # a1 >= s1-b1 >= s1-(s1-1)=1, similarly all a>=1, b>=0, so the spell with
    # maximum (a+b) dominates all others for every x>=1.
    best_spell_sum = 0
    best_spell_a = 1
    best_spell_b = 0
    for a, b in zip(sa, sb):
        s = a + b
        if s > best_spell_sum:
            best_spell_sum = s
            best_spell_a = a
            best_spell_b = b

    # Meals ordering:
    # For two effects f=(a,b), g=(c,d), f before g is better iff b*(c-1) <= d*(a-1).
    # Sort by this comparator.
    meals = list(zip(ma, mb))

    def cmp_key_item(item):
        return item

    from functools import cmp_to_key
    def meal_cmp(x, y):
        ax, bx = x
        ay, by = y
        left = bx * (ay - 1)
        right = by * (ax - 1)
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    meals.sort(key=cmp_to_key(meal_cmp))

    # Compose all meals into one affine transform x -> A_meal * x + B_meal
    A_meal_mod = 1
    B_meal_mod = 0
    for a, b in meals:
        A_meal_mod = (a % MOD) * A_meal_mod % MOD
        B_meal_mod = ((a % MOD) * B_meal_mod + b) % MOD

    # Spell repeated K times:
    # x -> a^K * x + b * (a^(K-1)+...+1)
    a = best_spell_a
    b = best_spell_b

    if K == 0:
        A_spell_mod = 1
        B_spell_mod = 0
    else:
        if a == 1:
            A_spell_mod = 1
            B_spell_mod = (b % MOD) * (K % MOD) % MOD
        else:
            A_spell_mod = pow(a % MOD, K, MOD)
            inv = pow((a - 1) % MOD, MOD - 2, MOD)
            geom = (A_spell_mod - 1) % MOD * inv % MOD
            B_spell_mod = (b % MOD) * geom % MOD

    # Total transform: meals after spells
    A_total = A_meal_mod * A_spell_mod % MOD
    B_total = (A_meal_mod * B_spell_mod + B_meal_mod) % MOD

    out = []
    for x in xs:
        out.append(str((A_total * (x % MOD) + B_total) % MOD))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()