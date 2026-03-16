#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

struct Line {
    ll a, b;
    int id;
};

struct Fenwick {
    int n;
    vector<long long> bit;
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }
    long long sumPrefix(int idx) const {
        long long r = 0;
        for (; idx > 0; idx -= idx & -idx) r += bit[idx];
        return r;
    }
};

static inline i128 valueAt(const Line& l, ll x) {
    return (i128)l.a * (i128)x + (i128)l.b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll X1, X2;
    cin >> N >> X1 >> X2;

    vector<Line> lines(N);
    for (int i = 0; i < N; ++i) {
        cin >> lines[i].a >> lines[i].b;
        lines[i].id = i;
    }

    auto cmpX1 = [&](const Line& p, const Line& q) {
        i128 vp = valueAt(p, X1);
        i128 vq = valueAt(q, X1);
        if (vp != vq) return vp < vq;
        return p.id < q.id;
    };

    auto cmpX2 = [&](const Line& p, const Line& q) {
        i128 vp = valueAt(p, X2);
        i128 vq = valueAt(q, X2);
        if (vp != vq) return vp < vq;
        return p.id < q.id;
    };

    vector<Line> ord1 = lines, ord2 = lines;
    sort(ord1.begin(), ord1.end(), cmpX1);
    sort(ord2.begin(), ord2.end(), cmpX2);

    vector<int> posInOrd2(N);
    for (int i = 0; i < N; ++i) posInOrd2[ord2[i].id] = i + 1;

    Fenwick fw(N);
    long long ans = 0;
    for (int i = 0; i < N; ++i) {
        int p = posInOrd2[ord1[i].id];
        ans += i - fw.sumPrefix(p);
        fw.add(p, 1);
    }

    cout << ans << '\n';
    return 0;
}