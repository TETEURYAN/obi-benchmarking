import sys

MOD = 10**9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    N = next(it)
    M = next(it)
    K = next(it)

    a_sp = [next(it) for _ in range(N)]
    b_sp = [next(it) for _ in range(N)]
    a_me = [next(it) for _ in range(M)]
    b_me = [next(it) for _ in range(M)]

    Q = next(it)
    xs = [next(it) for _ in range(Q)]

    # Best spell: maximize a*x+b for all x>=1
    # Since all a,b >=0 and x>=1, dominance by larger a, tie larger b.
    best_a = a_sp[0]
    best_b = b_sp[0]
    for a, b in zip(a_sp, b_sp):
        if a > best_a or (a == best_a and b > best_b):
            best_a, best_b = a, b

    # Meals: sort by decreasing b/(a-1), with a=1 first among themselves by larger b.
    meals = list(zip(a_me, b_me))

    def cmp_key(item):
        a, b = item
        if a == 1:
            return (0, -b)
        return (1, 0)

    ones = []
    others = []
    for a, b in meals:
        if a == 1:
            ones.append((a, b))
        else:
            others.append((a, b))

    ones.sort(key=lambda x: -x[1])

    def less(u, v):
        a1, b1 = u
        a2, b2 = v
        return b1 * (a2 - 1) > b2 * (a1 - 1)

    if others:
        import functools
        def cmp(u, v):
            a1, b1 = u
            a2, b2 = v
            left = b1 * (a2 - 1)
            right = b2 * (a1 - 1)
            if left > right:
                return -1
            if left < right:
                return 1
            return 0
        others.sort(key=functools.cmp_to_key(cmp))

    ordered = ones + others

    A_meal = 1
    B_meal = 0
    for a, b in ordered:
        A_meal = (a % MOD) * A_meal % MOD
        B_meal = ((a % MOD) * B_meal + b) % MOD

    # Spell composition repeated K times:
    # f(x)=a*x+b
    # f^K(x)=a^K*x + b*(a^(K-1)+...+1)
    if best_a == 1:
        A_spell = 1
        B_spell = (best_b % MOD) * (K % MOD) % MOD
    else:
        A_spell = pow(best_a % MOD, K, MOD)
        inv = pow((best_a - 1) % MOD, MOD - 2, MOD)
        geom = (A_spell - 1) % MOD * inv % MOD
        B_spell = (best_b % MOD) * geom % MOD

    A_total = A_meal * A_spell % MOD
    B_total = (A_meal * B_spell + B_meal) % MOD

    out = []
    for x in xs:
        out.append(str((A_total * (x % MOD) + B_total) % MOD))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
