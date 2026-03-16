#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

struct Fenwick {
    int n;
    vector<ll> bit;
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, ll val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }
    ll sumPrefix(int idx) const {
        ll r = 0;
        for (; idx > 0; idx -= idx & -idx) r += bit[idx];
        return r;
    }
};

struct Line {
    ll a, b;
    int id;
};

static inline i128 eval(const Line& l, ll x) {
    return (i128)l.a * (i128)x + (i128)l.b;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    ll X1, X2;
    if (!(cin >> N >> X1 >> X2)) return 0;

    vector<Line> lines(N);
    for (int i = 0; i < N; i++) {
        cin >> lines[i].a >> lines[i].b;
        lines[i].id = i;
    }

    auto cmpX1 = [&](const Line& l1, const Line& l2) {
        i128 y1 = eval(l1, X1);
        i128 y2 = eval(l2, X1);
        if (y1 != y2) return y1 < y2;
        return l1.id < l2.id;
    };

    auto cmpX2 = [&](const Line& l1, const Line& l2) {
        i128 y1 = eval(l1, X2);
        i128 y2 = eval(l2, X2);
        if (y1 != y2) return y1 < y2;
        return l1.id < l2.id;
    };

    vector<Line> ord1 = lines, ord2 = lines;
    stable_sort(ord1.begin(), ord1.end(), cmpX1);
    stable_sort(ord2.begin(), ord2.end(), cmpX2);

    vector<int> posInOrd2(N);
    for (int i = 0; i < N; i++) posInOrd2[ord2[i].id] = i + 1;

    Fenwick fw(N);
    ll ans = 0;
    for (int i = 0; i < N; i++) {
        int p = posInOrd2[ord1[i].id];
        ans += i - fw.sumPrefix(p);
        fw.add(p, 1);
    }

    cout << ans << '\n';
    return 0;
}