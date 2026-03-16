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
    i128 y1, y2;
};

static bool cmpY1(const Line& p, const Line& q) {
    if (p.y1 != q.y1) return p.y1 < q.y1;
    return p.y2 < q.y2;
}

static bool cmpY2(const Line& p, const Line& q) {
    if (p.y2 != q.y2) return p.y2 < q.y2;
    return p.y1 < q.y1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll X1, X2;
    cin >> N >> X1 >> X2;

    vector<Line> v(N);
    for (int i = 0; i < N; ++i) {
        ll a, b;
        cin >> a >> b;
        v[i] = {a, b, (i128)a * X1 + b, (i128)a * X2 + b};
    }

    sort(v.begin(), v.end(), cmpY1);

    vector<i128> vals;
    vals.reserve(N);
    for (auto &ln : v) vals.push_back(ln.y2);
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    Fenwick fw((int)vals.size());
    long long ans = 0;

    int i = 0;
    while (i < N) {
        int j = i;
        while (j < N && v[j].y1 == v[i].y1) j++;

        for (int k = i; k < j; ++k) {
            int pos = lower_bound(vals.begin(), vals.end(), v[k].y2) - vals.begin() + 1;
            ans += fw.sumPrefix(pos);
        }
        for (int k = i; k < j; ++k) {
            int pos = lower_bound(vals.begin(), vals.end(), v[k].y2) - vals.begin() + 1;
            fw.add(pos, 1);
        }

        i = j;
    }

    cout << ans << '\n';
    return 0;
}