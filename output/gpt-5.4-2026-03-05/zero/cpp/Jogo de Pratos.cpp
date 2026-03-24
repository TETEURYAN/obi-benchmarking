#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

static const int MOD = 1000000007;

struct Line {
    long long m, c;
};

static inline bool better(const pair<long long,long long>& A, const pair<long long,long long>& B){
    if (A.first != B.first) return A.first > B.first;
    return A.second > B.second;
}

static inline long long floor_div(i128 a, i128 b){
    // b > 0
    if (a >= 0) return (long long)(a / b);
    return (long long)(- ((-a + b - 1) / b));
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

    pair<long long,long long> bestSpell = {0, 0};
    for (int i = 0; i < N; ++i) {
        bestSpell = max(bestSpell, {as[i], bs[i]});
    }

    long long Aspell = bestSpell.first, Bspell = bestSpell.second;

    long long spellMulMod = 1, spellAddMod = 0;
    if (K > 0) {
        if (Aspell == 1) {
            spellMulMod = 1;
            spellAddMod = ( (__int128)(Bspell % MOD) * (K % MOD) ) % MOD;
        } else {
            long long p = 1, base = Aspell % MOD, e = K;
            while (e) {
                if (e & 1) p = (i128)p * base % MOD;
                base = (i128)base * base % MOD;
                e >>= 1;
            }
            spellMulMod = p;
            long long inv = 1, b = (Aspell - 1) % MOD, exp = MOD - 2;
            long long cur = b;
            while (exp) {
                if (exp & 1) inv = (i128)inv * cur % MOD;
                cur = (i128)cur * cur % MOD;
                exp >>= 1;
            }
            spellAddMod = (i128)(Bspell % MOD) * ((spellMulMod - 1 + MOD) % MOD) % MOD * inv % MOD;
        }
    }

    vector<pair<long long,long long>> meals(M);
    for (int i = 0; i < M; ++i) meals[i] = {am[i], bm[i]};

    sort(meals.begin(), meals.end(), [](const auto& p1, const auto& p2){
        i128 lhs = (i128)(p1.first - 1) * p2.second;
        i128 rhs = (i128)(p2.first - 1) * p1.second;
        if (lhs != rhs) return lhs > rhs;
        if (p1.first != p2.first) return p1.first > p2.first;
        return p1.second > p2.second;
    });

    long long mulMod = 1, addMod = 0;
    for (int i = 0; i < M; ++i) {
        mulMod = (i128)meals[i].first % MOD * mulMod % MOD;
        addMod = ((i128)meals[i].first % MOD * addMod + meals[i].second) % MOD;
    }

    int Q;
    cin >> Q;
    while (Q--) {
        long long x;
        cin >> x;
        long long afterSpells = ((i128)spellMulMod * (x % MOD) + spellAddMod) % MOD;
        long long ans = ((i128)mulMod * afterSpells + addMod) % MOD;
        cout << ans << '\n';
    }

    return 0;
}