#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Line {
    long long m, c;
};

static inline long long floor_div_i128(i128 a, i128 b) {
    if (b < 0) a = -a, b = -b;
    if (a >= 0) return (long long)(a / b);
    return (long long)(- ((-a + b - 1) / b));
}

static inline long long intersect_x(const Line& l1, const Line& l2) {
    i128 num = (i128)l1.c - (i128)l2.c;
    i128 den = (i128)l2.m - (i128)l1.m;
    return floor_div_i128(num, den);
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

    long long bestA = -1, bestB = -1;
    for (int i = 0; i < N; i++) {
        if (as[i] > bestA || (as[i] == bestA && bs[i] > bestB)) {
            bestA = as[i];
            bestB = bs[i];
        }
    }

    long long spellMulMod = 1;
    long long spellAddMod = 0;

    if (bestA == 1) {
        long long t = K % MOD;
        spellMulMod = 1;
        spellAddMod = ( (__int128)(bestB % MOD) * t ) % MOD;
    } else {
        long long A = bestA % MOD;
        long long B = bestB % MOD;
        long long p = 1, e = K;
        while (e) {
            if (e & 1) p = (long long)((__int128)p * A % MOD);
            A = (long long)((__int128)A * A % MOD);
            e >>= 1;
        }
        spellMulMod = p;
        long long inv = 1, base = (bestA - 1) % MOD, exp = MOD - 2;
        while (exp) {
            if (exp & 1) inv = (long long)((__int128)inv * base % MOD);
            base = (long long)((__int128)base * base % MOD);
            exp >>= 1;
        }
        spellAddMod = (long long)((__int128)(p - 1 + MOD) % MOD * B % MOD * inv % MOD);
    }

    vector<pair<long long,long long>> meals(M);
    for (int i = 0; i < M; i++) meals[i] = {am[i], bm[i]};
    sort(meals.begin(), meals.end(), [](const auto& x, const auto& y) {
        i128 lhs = (i128)(x.first - 1) * y.second;
        i128 rhs = (i128)(y.first - 1) * x.second;
        if (lhs != rhs) return lhs > rhs;
        if (x.first != y.first) return x.first > y.first;
        return x.second > y.second;
    });

    vector<Line> hull;
    vector<long long> startX;

    long long curMmod = 1, curCmod = 0;

    for (int i = M - 1; i >= 0; i--) {
        long long a = meals[i].first;
        long long b = meals[i].second;

        long long newMmod = (long long)((__int128)(a % MOD) * curMmod % MOD);
        long long newCmod = ((long long)((__int128)(a % MOD) * curCmod % MOD) + b) % MOD;
        curMmod = newMmod;
        curCmod = newCmod;

        Line nl{curMmod, curCmod};

        if (!hull.empty() && hull.back().m == nl.m) {
            if (hull.back().c >= nl.c) continue;
            hull.pop_back();
            if (!startX.empty()) startX.pop_back();
        }

        while (!hull.empty()) {
            long long x = intersect_x(hull.back(), nl);
            if (startX.empty() || x > startX.back()) {
                startX.push_back(x + 1);
                hull.push_back(nl);
                break;
            } else {
                hull.pop_back();
                startX.pop_back();
            }
        }
        if (hull.empty()) {
            hull.push_back(nl);
        }
    }

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;

        long long y = ((long long)((__int128)(x % MOD) * spellMulMod % MOD) + spellAddMod) % MOD;

        int idx = upper_bound(startX.begin(), startX.end(), y) - startX.begin();
        long long ans = ((long long)((__int128)hull[idx].m * y % MOD) + hull[idx].c) % MOD;
        cout << ans << '\n';
    }

    return 0;
}