#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Effect {
    long long a, b;
};

static inline bool betterForAll(const Effect& x, const Effect& y) {
    // x(t) >= y(t) for all t >= 1  <=>  (ax-ay)*1 + (bx-by) >= 0 and ax>=ay
    return x.a >= y.a && x.a + x.b >= y.a + y.b;
}

static vector<Effect> pruneSpells(const vector<Effect>& v) {
    vector<Effect> arr = v;
    sort(arr.begin(), arr.end(), [](const Effect& x, const Effect& y){
        if (x.a != y.a) return x.a > y.a;
        return x.b > y.b;
    });
    vector<Effect> res;
    long long bestSum = -1;
    for (auto &e : arr) {
        long long s = e.a + e.b;
        if (s > bestSum) {
            res.push_back(e);
            bestSum = s;
        }
    }
    return res;
}

static vector<Effect> sortMealsOptimal(vector<Effect> meals) {
    sort(meals.begin(), meals.end(), [](const Effect& x, const Effect& y){
        i128 lhs = (i128)(x.a - 1) * y.b;
        i128 rhs = (i128)(y.a - 1) * x.b;
        if (lhs != rhs) return lhs > rhs;
        if (x.a != y.a) return x.a > y.a;
        return x.b > y.b;
    });
    return meals;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    long long K;
    cin >> N >> M >> K;

    vector<long long> a(N), b(N), am(M), bm(M);
    for (int i = 0; i < N; ++i) cin >> a[i];
    for (int i = 0; i < N; ++i) cin >> b[i];
    for (int i = 0; i < M; ++i) cin >> am[i];
    for (int i = 0; i < M; ++i) cin >> bm[i];

    vector<Effect> spells(N), meals(M);
    for (int i = 0; i < N; ++i) spells[i] = {a[i], b[i]};
    for (int i = 0; i < M; ++i) meals[i] = {am[i], bm[i]};

    vector<Effect> goodSpells = pruneSpells(spells);

    auto bestSpellAt = [&](long long x)->Effect{
        int l = 0, r = (int)goodSpells.size() - 1;
        while (l < r) {
            int m = (l + r) >> 1;
            i128 v1 = (i128)goodSpells[m].a * x + goodSpells[m].b;
            i128 v2 = (i128)goodSpells[m+1].a * x + goodSpells[m+1].b;
            if (v2 >= v1) l = m + 1;
            else r = m;
        }
        return goodSpells[l];
    };

    vector<Effect> orderedMeals = sortMealsOptimal(meals);

    long long AmealMod = 1;
    long long BmealMod = 0;
    for (auto &e : orderedMeals) {
        AmealMod = (AmealMod * (e.a % MOD)) % MOD;
        BmealMod = ((e.a % MOD) * BmealMod + (e.b % MOD)) % MOD;
    }

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;

        long long curMod = x % MOD;
        long long curReal = x;

        for (long long step = 0; step < K; ++step) {
            Effect best = bestSpellAt(curReal);
            if (best.a == 1) {
                long long times = K - step;
                curMod = (curMod + (times % MOD) * (best.b % MOD)) % MOD;
                curReal += times * best.b;
                break;
            } else {
                curMod = ((best.a % MOD) * curMod + (best.b % MOD)) % MOD;
                if (curReal > (long long)4e18 / best.a) {
                    curReal = (long long)4e18;
                } else {
                    curReal = best.a * curReal + best.b;
                    if (curReal > (long long)4e18) curReal = (long long)4e18;
                }
            }
        }

        long long ans = (AmealMod * curMod + BmealMod) % MOD;
        cout << ans << '\n';
    }

    return 0;
}