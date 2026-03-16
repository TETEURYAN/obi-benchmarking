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
    ll y1, y2;
};

static bool cmpY1(const Line& p, const Line& q) {
    if (p.y1 != q.y1) return p.y1 < q.y1;
    if (p.y2 != q.y2) return p.y2 < q.y2;
    if (p.a != q.a) return p.a < q.a;
    return p.b < q.b;
}

static bool cmpY2(const Line& p, const Line& q) {
    if (p.y2 != q.y2) return p.y2 < q.y2;
    if (p.y1 != q.y1) return p.y1 < q.y1;
    if (p.a != q.a) return p.a < q.a;
    return p.b < q.b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll X1, X2;
    if (!(cin >> N >> X1 >> X2)) return 0;

    vector<Line> lines(N);
    for (int i = 0; i < N; i++) {
        ll a, b;
        cin >> a >> b;
        lines[i] = {a, b, a * X1 + b, a * X2 + b};
    }

    vector<Line> by1 = lines, by2 = lines;
    sort(by1.begin(), by1.end(), cmpY1);
    sort(by2.begin(), by2.end(), cmpY2);

    map<pair<ll,ll>, vector<int>> posBy2;
    for (int i = 0; i < N; i++) {
        posBy2[{by2[i].y1, by2[i].y2}].push_back(i + 1);
    }

    map<pair<ll,ll>, int> used;
    vector<int> perm(N);
    for (int i = 0; i < N; i++) {
        auto key = make_pair(by1[i].y1, by1[i].y2);
        int &u = used[key];
        perm[i] = posBy2[key][u++];
    }

    Fenwick fw(N);
    ll inv = 0;
    for (int i = N - 1; i >= 0; i--) {
        inv += fw.sumPrefix(perm[i] - 1);
        fw.add(perm[i], 1);
    }

    ll equalAtBoth = 0;
    int i = 0;
    while (i < N) {
        int j = i;
        while (j < N && by1[j].y1 == by1[i].y1 && by1[j].y2 == by1[i].y2) j++;
        ll k = j - i;
        equalAtBoth += k * (k - 1) / 2;
        i = j;
    }

    cout << (inv + equalAtBoth) << '\n';
    return 0;
}