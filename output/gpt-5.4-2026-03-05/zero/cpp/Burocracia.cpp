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
    vector<vector<int>> g(N + 1);
    parent[1] = 0;
    for (int i = 2; i <= N; i++) {
        cin >> parent[i];
        g[parent[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1), euler(N + 1);
    int timer = 0;
    vector<int> st;
    st.push_back(1);
    vector<int> it(N + 1, 0);
    depth[1] = 0;

    while (!st.empty()) {
        int v = st.back();
        if (it[v] == 0) {
            tin[v] = ++timer;
            euler[timer] = v;
        }
        if (it[v] < (int)g[v].size()) {
            int u = g[v][it[v]++];
            depth[u] = depth[v] + 1;
            st.push_back(u);
        } else {
            tout[v] = timer;
            st.pop_back();
        }
    }

    int LOG = 1;
    while ((1 << LOG) <= N) LOG++;
    vector<vector<int>> up(LOG, vector<int>(N + 1, 0));
    for (int v = 1; v <= N; v++) up[0][v] = parent[v];
    for (int j = 1; j < LOG; j++) {
        for (int v = 1; v <= N; v++) {
            up[j][v] = up[j - 1][ up[j - 1][v] ];
        }
    }

    auto kthAncestorOriginal = [&](int v, int k) {
        for (int j = 0; j < LOG; j++) {
            if (k & (1 << j)) v = up[j][v];
        }
        return v;
    };

    Fenwick bit(N);
    vector<int> restructured(N + 1, 0);

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 2) {
            int v;
            cin >> v;
            if (!restructured[v]) {
                restructured[v] = 1;
                bit.add(tin[v], 1);
                bit.add(tout[v] + 1, -1);
            }
        } else {
            int v, k;
            cin >> v >> k;

            int x = v;
            while (k > 0) {
                int cnt = bit.sumPrefix(tin[x]);
                int lo = 1, hi = depth[x], best = 0;
                while (lo <= hi) {
                    int mid = (lo + hi) >> 1;
                    int a = kthAncestorOriginal(x, mid);
                    int c = bit.sumPrefix(tin[a]);
                    if (c == cnt) {
                        best = mid;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }

                if (best >= k) {
                    x = kthAncestorOriginal(x, k);
                    k = 0;
                } else {
                    x = kthAncestorOriginal(x, best);
                    k -= best;
                    if (k == 0) break;
                    int y = x;
                    while (true) {
                        int p = parent[y];
                        if (bit.sumPrefix(tin[p]) < bit.sumPrefix(tin[y])) {
                            x = p;
                            break;
                        }
                        y = p;
                    }
                    k--;
                }
            }

            cout << x << '\n';
        }
    }

    return 0;
}