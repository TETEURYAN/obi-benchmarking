import sys

MOD = 10**9 + 7

def better(f1, f2):
    a1, b1 = f1
    a2, b2 = f2
    if a1 == a2:
        return b1 > b2
    if a1 > a2:
        return b1 * (a2 - 1) >= b2 * (a1 - 1)
    else:
        return b2 * (a1 - 1) <= b1 * (a2 - 1)

def compose(f, g):
    a1, b1 = f
    a2, b2 = g
    return (a2 * a1, a2 * b1 + b2)

def mat_mul(A, B):
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ],
    ]

def mat_vec(A, v):
    return (
        A[0][0] * v[0] + A[0][1] * v[1],
        A[1][0] * v[0] + A[1][1] * v[1],
    )

def mat_mul_mod(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD,
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD,
        ],
    ]

def mat_pow_mod(base, exp):
    res = [[1, 0], [0, 1]]
    while exp:
        if exp & 1:
            res = mat_mul_mod(res, base)
        base = mat_mul_mod(base, base)
        exp >>= 1
    return res

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    sa = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    ma = list(map(int, input().split()))
    mb = list(map(int, input().split()))
    Q = int(input())
    xs = list(map(int, input().split()))

    best_spell = (sa[0], sb[0])
    for i in range(1, N):
        cur = (sa[i], sb[i])
        if better(cur, best_spell):
            best_spell = cur

    meals = list(zip(ma, mb))
    meals.sort(key=lambda p: (p[0] - 1) / p[1] if p[0] == 1 and p[1] > 0 else 0)

    def meal_cmp_key(item):
        a, b = item
        return (a, b)

    from functools import cmp_to_key
    def cmp(x, y):
        a1, b1 = x
        a2, b2 = y
        left = b1 * (a2 - 1)
        right = b2 * (a1 - 1)
        if left > right:
            return -1
        if left < right:
            return 1
        return 0

    meals.sort(key=cmp_to_key(cmp))

    meal_total = (1, 0)
    for f in meals:
        meal_total = compose(meal_total, f)

    a_s, b_s = best_spell
    spell_mat = [[a_s, b_s], [0, 1]]
    spell_pow_mod = mat_pow_mod(spell_mat, K)

    if a_s == 1:
        spell_total = (1, b_s * K)
    else:
        spell_total = None

    meal_a_mod = meal_total[0] % MOD
    meal_b_mod = meal_total[1] % MOD

    out = []
    for x in xs:
        if a_s == 1:
            y_mod = (x + (b_s % MOD) * (K % MOD)) % MOD
        else:
            y_mod = (spell_pow_mod[0][0] * (x % MOD) + spell_pow_mod[0][1]) % MOD
        ans = (meal_a_mod * y_mod + meal_b_mod) % MOD
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
