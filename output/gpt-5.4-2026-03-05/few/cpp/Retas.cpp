#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

struct Line {
    ll a, b;
    ll y1, y2;
    int id;
};

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
    ll sumRange(int l, int r) const {
        if (l > r) return 0;
        return sumPrefix(r) - sumPrefix(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll X1, X2;
    if (!(cin >> N >> X1 >> X2)) return 0;

    vector<Line> lines(N);
    vector<ll> vals;
    vals.reserve(2 * N);

    for (int i = 0; i < N; ++i) {
        ll a, b;
        cin >> a >> b;
        i128 v1 = (i128)a * X1 + b;
        i128 v2 = (i128)a * X2 + b;
        lines[i] = {a, b, (ll)v1, (ll)v2, i};
        vals.push_back((ll)v2);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto getPos = [&](ll v) {
        return (int)(lower_bound(vals.begin(), vals.end(), v) - vals.begin()) + 1;
    };

    sort(lines.begin(), lines.end(), [&](const Line& p, const Line& q) {
        if (p.y1 != q.y1) return p.y1 < q.y1;
        return p.y2 < q.y2;
    });

    ll ans = 0;
    Fenwick fw((int)vals.size());

    int i = 0;
    while (i < N) {
        int j = i;
        while (j < N && lines[j].y1 == lines[i].y1) j++;

        unordered_map<ll, int> freq;
        freq.reserve((j - i) * 2 + 1);
        for (int k = i; k < j; ++k) freq[lines[k].y2]++;

        ll processed = 0;
        for (auto &it : freq) {
            ll c = it.second;
            ans += c * processed;
            processed += c;
        }

        for (int k = i; k < j; ++k) {
            int pos = getPos(lines[k].y2);
            ans += fw.sumRange(pos, (int)vals.size());
        }

        for (int k = i; k < j; ++k) {
            int pos = getPos(lines[k].y2);
            fw.add(pos, 1);
        }

        i = j;
    }

    cout << ans << '\n';
    return 0;
}