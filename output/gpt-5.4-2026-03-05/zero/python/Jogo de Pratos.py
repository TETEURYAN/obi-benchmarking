import sys

MOD = 10**9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
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

    # Best spell for repeated use:
    # maximize a*x+b for all x>=1
    # Since all a,b >=0 and x>=1, if a1>=a2 and b1>=b2 then 1 dominates 2.
    # The global optimum is the spell with maximum (a+b), tie by larger a.
    best_idx = 0
    best_sum = sa[0] + sb[0]
    best_a = sa[0]
    for i in range(1, N):
        s = sa[i] + sb[i]
        if s > best_sum or (s == best_sum and sa[i] > best_a):
            best_sum = s
            best_a = sa[i]
            best_idx = i

    A = sa[best_idx]
    B = sb[best_idx]

    # Meals: sort by comparator of affine composition
    meals = list(zip(ma, mb))
    meals.sort(key=lambda p: (0,))  # placeholder to avoid lint

    from functools import cmp_to_key
    def cmp(e1, e2):
        a1, b1 = e1
        a2, b2 = e2
        v = b1 * (a2 - 1) - b2 * (a1 - 1)
        if v > 0:
            return -1
        if v < 0:
            return 1
        return 0

    meals.sort(key=cmp_to_key(cmp))

    # Compose all meals into y = P*x + Qc
    P = 1
    Qc = 0
    for a, b in meals:
        P = (a * P) % MOD
        Qc = (a * Qc + b) % MOD

    # Spell repeated K times:
    # if A == 1: x -> x + K*B
    # else: x -> A^K * x + B*(A^K - 1)/(A-1)
    if A == 1:
        spell_mul = 1
        spell_add = (K % MOD) * (B % MOD) % MOD
    else:
        spell_mul = pow(A % MOD, K, MOD)
        denom_inv = pow((A - 1) % MOD, MOD - 2, MOD)
        spell_add = (B % MOD) * ((spell_mul - 1) % MOD) % MOD * denom_inv % MOD

    out = []
    for x in xs:
        y = (spell_mul * (x % MOD) + spell_add) % MOD
        ans = (P * y + Qc) % MOD
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
