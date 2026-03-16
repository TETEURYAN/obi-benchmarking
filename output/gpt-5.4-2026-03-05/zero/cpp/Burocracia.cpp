#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick() {}
    Fenwick(int n): n(n), bit(n + 1, 0) {}
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> parent(N + 1, 0);
    vector<vector<int>> children(N + 1);
    parent[1] = 0;
    for (int i = 2; i <= N; i++) {
        cin >> parent[i];
        children[parent[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1), euler(N + 1);
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
            euler[timer] = u;
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

    vector<vector<int>> byDepth(N + 1);
    for (int i = 1; i <= N; i++) byDepth[depth[i]].push_back(tin[i]);

    int Q;
    cin >> Q;

    Fenwick fw(N);
    vector<char> active(N + 1, 0);
    active[1] = 1;
    fw.add(tin[1], 1);

    auto countActiveAnc = [&](int v) {
        return fw.sumPrefix(tin[v]);
    };

    auto findKthActiveAncestor = [&](int v, int k) {
        int target = countActiveAnc(v) - k;
        int cur = v;
        for (int j = LOG - 1; j >= 0; j--) {
            int a = up[j][cur];
            if (a != 0 && countActiveAnc(a) > target) {
                cur = a;
            }
        }
        return up[0][cur];
    };

    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            cout << findKthActiveAncestor(v, k) << '\n';
        } else {
            int v;
            cin >> v;
            int dv = depth[v];
            int l = tin[v], r = tout[v];
            for (int d = dv + 1; d <= N; d++) {
                auto &vec = byDepth[d];
                if (vec.empty()) continue;
                auto it1 = lower_bound(vec.begin(), vec.end(), l);
                auto it2 = upper_bound(vec.begin(), vec.end(), r);
                for (auto it = it1; it != it2; ++it) {
                    int u = euler[*it];
                    if (!active[u]) {
                        active[u] = 1;
                        fw.add(*it, 1);
                    }
                }
            }
        }
    }

    return 0;
}