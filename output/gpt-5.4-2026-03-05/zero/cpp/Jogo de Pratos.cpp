#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Effect {
    long long a, b;
};

static inline bool betterForAll(const Effect& x, const Effect& y) {
    return x.a >= y.a && x.b >= y.b && (x.a > y.a || x.b > y.b);
}

static inline bool cmpMeal(const Effect& p, const Effect& q) {
    i128 lhs = (i128)(p.a - 1) * q.b;
    i128 rhs = (i128)(q.a - 1) * p.b;
    if (lhs != rhs) return lhs > rhs;
    if (p.a != q.a) return p.a > q.a;
    return p.b > q.b;
}

static inline long long modmul(long long a, long long b) {
    return (long long)((__int128)a * b % MOD);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    long long K;
    cin >> N >> M >> K;

    vector<long long> as(N), bs(N), am(M), bm(M);
    for (int i = 0; i < N; ++i) cin >> as[i];
    for (int i = 0; i < N; ++i) cin >> bs[i];
    for (int i = 0; i < M; ++i) cin >> am[i];
    for (int i = 0; i < M; ++i) cin >> bm[i];

    vector<Effect> spells(N), meals(M);
    for (int i = 0; i < N; ++i) spells[i] = {as[i], bs[i]};
    for (int i = 0; i < M; ++i) meals[i] = {am[i], bm[i]};

    Effect bestSpell = spells[0];
    for (int i = 1; i < N; ++i) {
        if (betterForAll(spells[i], bestSpell)) bestSpell = spells[i];
    }

    sort(meals.begin(), meals.end(), cmpMeal);

    vector<Effect> filtered;
    filtered.reserve(M);
    for (auto &e : meals) {
        while (!filtered.empty() && betterForAll(e, filtered.back())) filtered.pop_back();
        filtered.push_back(e);
    }

    int L = (int)filtered.size();

    vector<long long> sufAmod(L + 1, 1), sufBmod(L + 1, 0);
    for (int i = L - 1; i >= 0; --i) {
        sufAmod[i] = modmul(filtered[i].a % MOD, sufAmod[i + 1]);
        sufBmod[i] = (modmul(filtered[i].a % MOD, sufBmod[i + 1]) + filtered[i].b % MOD) % MOD;
    }

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;

        int useMealsFrom = 0;
        long long cur = x;

        for (int i = 0; i < L; ++i) {
            i128 withSpell = (i128)bestSpell.a * cur + bestSpell.b;
            i128 withMeal = (i128)filtered[i].a * cur + filtered[i].b;
            if (withSpell > withMeal && K > 0) {
                cur = (long long)withSpell;
            } else {
                useMealsFrom = i;
                break;
            }
            if (i == L - 1) useMealsFrom = L;
        }

        long long ans;
        if (useMealsFrom == L) {
            long long A = 1, B = 0;
            long long a = bestSpell.a % MOD, b = bestSpell.b % MOD;
            long long e = K;
            while (e > 0) {
                if (e & 1) {
                    B = (modmul(a, B) + b) % MOD;
                    A = modmul(a, A);
                }
                b = (modmul(a, b) + b) % MOD;
                a = modmul(a, a);
                e >>= 1;
            }
            ans = (modmul(A, x % MOD) + B) % MOD;
        } else {
            long long usedSpells = 0;
            cur = x;
            while (usedSpells < K) {
                i128 withSpell = (i128)bestSpell.a * cur + bestSpell.b;
                i128 withMeal = (i128)filtered[useMealsFrom].a * cur + filtered[useMealsFrom].b;
                if (withSpell > withMeal) {
                    cur = (long long)withSpell;
                    ++usedSpells;
                } else break;
            }

            long long A = 1, B = 0;
            long long a = bestSpell.a % MOD, b = bestSpell.b % MOD;
            long long e = usedSpells;
            while (e > 0) {
                if (e & 1) {
                    B = (modmul(a, B) + b) % MOD;
                    A = modmul(a, A);
                }
                b = (modmul(a, b) + b) % MOD;
                a = modmul(a, a);
                e >>= 1;
            }

            long long afterSpells = (modmul(A, x % MOD) + B) % MOD;
            ans = (modmul(sufAmod[useMealsFrom], afterSpells) + sufBmod[useMealsFrom]) % MOD;
        }

        cout << ans % MOD << '\n';
    }

    return 0;
}