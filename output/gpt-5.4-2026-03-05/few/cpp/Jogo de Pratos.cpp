#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Effect {
    long long a, b;
};

static inline long long mod_mul(long long a, long long b) {
    return (long long)((__int128)a * b % MOD);
}

static inline bool betterAt1(const Effect& x, const Effect& y) {
    i128 lx = (i128)x.a + x.b;
    i128 ly = (i128)y.a + y.b;
    if (lx != ly) return lx > ly;
    if (x.a != y.a) return x.a > y.a;
    return x.b > y.b;
}

static inline bool mealCmp(const Effect& x, const Effect& y) {
    i128 lhs = (i128)(x.a - 1) * y.b;
    i128 rhs = (i128)(y.a - 1) * x.b;
    if (lhs != rhs) return lhs > rhs;
    if (x.a != y.a) return x.a > y.a;
    return x.b > y.b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    long long K;
    cin >> N >> M >> K;

    vector<long long> as(N), bs(N), am(M), bm(M);
    for (int i = 0; i < N; i++) cin >> as[i];
    for (int i = 0; i < N; i++) cin >> bs[i];
    for (int i = 0; i < M; i++) cin >> am[i];
    for (int i = 0; i < M; i++) cin >> bm[i];

    vector<Effect> spells(N), meals(M);
    for (int i = 0; i < N; i++) spells[i] = {as[i], bs[i]};
    for (int i = 0; i < M; i++) meals[i] = {am[i], bm[i]};

    Effect bestSpell = spells[0];
    for (int i = 1; i < N; i++) {
        if (betterAt1(spells[i], bestSpell)) bestSpell = spells[i];
    }

    sort(meals.begin(), meals.end(), mealCmp);

    long long AmealMod = 1;
    long long BmealMod = 0;
    for (int i = 0; i < M; i++) {
        AmealMod = mod_mul(AmealMod, meals[i].a % MOD);
        BmealMod = (mod_mul(meals[i].a % MOD, BmealMod) + meals[i].b % MOD) % MOD;
    }

    long long asp = bestSpell.a, bsp = bestSpell.b;

    long long AkMod, BkMod;
    if (asp == 1) {
        AkMod = 1;
        BkMod = ( (__int128)(K % MOD) * (bsp % MOD) ) % MOD;
    } else {
        long long aMod = asp % MOD;
        long long powA = 1, base = aMod, exp = K;
        while (exp > 0) {
            if (exp & 1) powA = mod_mul(powA, base);
            base = mod_mul(base, base);
            exp >>= 1;
        }
        AkMod = powA;
        long long num = (AkMod - 1 + MOD) % MOD;
        long long den = (aMod - 1 + MOD) % MOD;
        long long e = MOD - 2, inv = 1, p = den;
        while (e > 0) {
            if (e & 1) inv = mod_mul(inv, p);
            p = mod_mul(p, p);
            e >>= 1;
        }
        BkMod = mod_mul(bsp % MOD, mod_mul(num, inv));
    }

    long long Afinal = mod_mul(AmealMod, AkMod);
    long long Bfinal = (mod_mul(AmealMod, BkMod) + BmealMod) % MOD;

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;
        long long ans = (mod_mul(Afinal, x % MOD) + Bfinal) % MOD;
        cout << ans << '\n';
    }

    return 0;
}