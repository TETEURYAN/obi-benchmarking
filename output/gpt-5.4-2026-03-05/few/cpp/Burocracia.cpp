#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick() {}
    Fenwick(int n) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }
    int sumPrefix(int idx) const {
        int r = 0;
        for (; idx > 0; idx -= idx & -idx) r += bit[idx];
        return r;
    }
    int rangeSum(int l, int r) const {
        if (l > r) return 0;
        return sumPrefix(r) - sumPrefix(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> parent(N + 1, 0);
    vector<vector<int>> children(N + 1);
    parent[1] = 0;
    for (int i = 2; i <= N; i++) {
        cin >> parent[i];
        children[parent[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1);
    vector<vector<int>> byDepth(N + 1);

    int timer = 0;
    vector<pair<int,int>> st;
    st.reserve(2 * N);
    st.push_back({1, 0});
    depth[1] = 0;

    while (!st.empty()) {
        auto [u, state] = st.back();
        st.pop_back();
        if (state == 0) {
            tin[u] = ++timer;
            byDepth[depth[u]].push_back(tin[u]);
            st.push_back({u, 1});
            for (int i = (int)children[u].size() - 1; i >= 0; i--) {
                int v = children[u][i];
                depth[v] = depth[u] + 1;
                st.push_back({v, 0});
            }
        } else {
            tout[u] = timer;
        }
    }

    int LOG = 1;
    while ((1 << LOG) <= N) LOG++;
    vector<vector<int>> up(LOG, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; i++) up[0][i] = parent[i];
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= N; i++) {
            up[j][i] = up[j - 1][ up[j - 1][i] ];
        }
    }

    auto kthAncestorOriginal = [&](int v, int k) {
        for (int j = 0; j < LOG; j++) {
            if (k & (1 << j)) v = up[j][v];
        }
        return v;
    };

    int Q;
    cin >> Q;

    Fenwick bit(N);
    vector<int> restructured(N + 1, 0);

    auto isRestructuredOnPathStrict = [&](int a, int b) {
        if (depth[a] + 1 > depth[b]) return false;
        int d = depth[b] - depth[a];
        auto &vec = byDepth[depth[a] + 1];
        int l = lower_bound(vec.begin(), vec.end(), tin[a]) - vec.begin();
        int r = upper_bound(vec.begin(), vec.end(), tout[a]) - vec.begin();
        if (l >= r) return false;
        int cnt = bit.rangeSum(l + 1, r);
        return cnt > 0;
    };

    string out;
    out.reserve(Q * 3);

    for (int qi = 0; qi < Q; qi++) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;

            int targetDepth = depth[v] - k;
            int lo = 0, hi = k, ans = 0;
            while (lo <= hi) {
                int mid = (lo + hi) >> 1;
                int anc = kthAncestorOriginal(v, mid);
                if (!isRestructuredOnPathStrict(anc, v)) {
                    ans = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }

            int x = kthAncestorOriginal(v, ans);
            if (ans == k) {
                out += to_string(x);
                out += '\n';
            } else {
                int rem = k - ans;
                int y = kthAncestorOriginal(v, ans + 1);
                int cur = y;
                if (rem == 1) {
                    out += to_string(cur);
                    out += '\n';
                } else {
                    int finalAns = kthAncestorOriginal(cur, rem - 1);
                    out += to_string(finalAns);
                    out += '\n';
                }
            }
        } else {
            int v;
            cin >> v;
            if (v != 1 && !restructured[v]) {
                restructured[v] = 1;
                int d = depth[v];
                int pos = lower_bound(byDepth[d].begin(), byDepth[d].end(), tin[v]) - byDepth[d].begin() + 1;
                bit.add(pos, 1);
            }
        }
    }

    cout << out;
    return 0;
}