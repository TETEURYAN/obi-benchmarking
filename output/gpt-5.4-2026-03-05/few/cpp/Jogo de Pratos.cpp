#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Line {
    long long m, c;
};

static inline long long floor_div_i128(i128 a, i128 b) {
    // b > 0
    if (a >= 0) return (long long)(a / b);
    return (long long)(- ((-a + b - 1) / b));
}

static inline long long intersect_x(const Line& l1, const Line& l2) {
    // smallest integer x such that l2(x) >= l1(x)
    // assume l2.m > l1.m
    i128 num = (i128)l1.c - (i128)l2.c;
    i128 den = (i128)l2.m - (i128)l1.m;
    return floor_div_i128(num, den) + 1;
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

    vector<pair<long long,long long>> meals(M);
    for (int i = 0; i < M; i++) meals[i] = {am[i], bm[i]};

    sort(meals.begin(), meals.end(), [](const auto& p1, const auto& p2) {
        i128 lhs = (i128)(p1.first - 1) * p2.second;
        i128 rhs = (i128)(p2.first - 1) * p1.second;
        if (lhs != rhs) return lhs > rhs;
        if (p1.first != p2.first) return p1.first > p2.first;
        return p1.second > p2.second;
    });

    long long Ameal_mod = 1;
    long long Bmeal_mod = 0;
    for (auto &p : meals) {
        long long a = p.first % MOD;
        long long b = p.second % MOD;
        Bmeal_mod = ((i128)a * Bmeal_mod + b) % MOD;
        Ameal_mod = (i128)Ameal_mod * a % MOD;
    }

    vector<Line> lines;
    vector<long long> starts;

    if (bestA == 1) {
        long long t = K;
        long long m = Ameal_mod;
        long long c = ((i128)Ameal_mod * ((t % MOD) * (bestB % MOD) % MOD) + Bmeal_mod) % MOD;
        lines.push_back({m, c});
        starts.push_back(1);
    } else {
        long long limit = 0;
        if (bestB == 0) {
            limit = 0;
        } else {
            i128 num = (i128)bestB;
            i128 den = (i128)bestA - 1;
            limit = (long long)(num / den);
        }

        long long t0 = 0;
        if (K > 0) {
            long long cur = 1;
            while (t0 < K && cur <= limit) {
                if (cur > (LLONG_MAX - bestB) / bestA) break;
                cur = bestA * cur + bestB;
                t0++;
            }
        }

        vector<Line> temp;
        temp.reserve((size_t)(K - t0 + 1));

        long long powA = 1 % MOD;
        for (long long i = 0; i < t0; i++) powA = (i128)powA * (bestA % MOD) % MOD;

        long long x0_mod = 1;
        for (long long i = 0; i < t0; i++) {
            x0_mod = ((i128)(bestA % MOD) * x0_mod + (bestB % MOD)) % MOD;
        }

        long long invAm1 = 1;
        {
            long long base = (bestA - 1) % MOD;
            long long exp = MOD - 2;
            long long res = 1;
            while (exp) {
                if (exp & 1) res = (i128)res * base % MOD;
                base = (i128)base * base % MOD;
                exp >>= 1;
            }
            invAm1 = res;
        }

        for (long long t = t0; t <= K; t++) {
            long long m = (i128)Ameal_mod * powA % MOD;
            long long cspell = ((x0_mod - (i128)powA) % MOD + MOD) % MOD;
            cspell = (i128)cspell * invAm1 % MOD;
            cspell = (i128)cspell * (bestB % MOD) % MOD;
            long long c = ((i128)Ameal_mod * cspell + Bmeal_mod) % MOD;
            temp.push_back({m, c});

            if (t != K) {
                powA = (i128)powA * (bestA % MOD) % MOD;
                x0_mod = ((i128)(bestA % MOD) * x0_mod + (bestB % MOD)) % MOD;
            }
        }

        for (auto &ln : temp) {
            if (!lines.empty() && lines.back().m == ln.m) {
                lines.back().c = max(lines.back().c, ln.c);
                continue;
            }
            while (lines.size() >= 2) {
                long long x1 = intersect_x(lines[lines.size()-2], lines[lines.size()-1]);
                long long x2 = intersect_x(lines[lines.size()-1], ln);
                if (x2 <= x1) {
                    lines.pop_back();
                    starts.pop_back();
                } else break;
            }
            if (lines.empty()) starts.push_back(1);
            else starts.push_back(intersect_x(lines.back(), ln));
            lines.push_back(ln);
        }
    }

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;
        int idx = (int)(upper_bound(starts.begin(), starts.end(), x) - starts.begin()) - 1;
        if (idx < 0) idx = 0;
        long long ans = ((i128)lines[idx].m * (x % MOD) + lines[idx].c) % MOD;
        cout << ans << '\n';
    }

    return 0;
}