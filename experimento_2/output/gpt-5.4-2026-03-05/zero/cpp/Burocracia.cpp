
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
    for (int i = 2; i <= N; ++i) {
        cin >> parent[i];
        children[parent[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1), euler(N + 1);
    int timer = 0;
    vector<pair<int,int>> st;
    st.push_back({1, 0});
    depth[1] = 0;
    while (!st.empty()) {
        auto [u, state] = st.back();
        st.pop_back();
        if (state == 0) {
            tin[u] = ++timer;
            euler[timer] = u;
            st.push_back({u, 1});
            for (int i = (int)children[u].size() - 1; i >= 0; --i) {
                int v = children[u][i];
                depth[v] = depth[u] + 1;
                st.push_back({v, 0});
            }
        } else {
            tout[u] = timer;
        }
    }

    int LOG = 1;
    while ((1 << LOG) <= N) ++LOG;
    vector<vector<int>> up(LOG, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; ++i) up[0][i] = parent[i];
    for (int j = 1; j < LOG; ++j) {
        for (int i = 1; i <= N; ++i) {
            up[j][i] = up[j - 1][ up[j - 1][i] ];
        }
    }

    auto kthAncestorOriginal = [&](int v, int k) {
        for (int j = 0; j < LOG; ++j) {
            if (k & (1 << j)) v = up[j][v];
        }
        return v;
    };

    vector<vector<int>> byDepth(N + 1);
    for (int i = 1; i <= N; ++i) byDepth[depth[i]].push_back(tin[i]);

    int Q;
    cin >> Q;

    Fenwick fw(N);
    vector<int> restructured(N + 1, 0);

    auto nearestRestructuredAncestor = [&](int v) {
        int l = 1, r = depth[v], ansDepth = 0;
        while (l <= r) {
            int mid = (l + r) >> 1;
            int anc = kthAncestorOriginal(v, depth[v] - mid);
            if (fw.rangeSum(tin[anc], tin[v]) > 0) {
                ansDepth = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        if (ansDepth == 0) return 0;
        return kthAncestorOriginal(v, depth[v] - ansDepth);
    };

    while (Q--) {
        int type;
        cin >> type;
        if (type == 2) {
            int v;
            cin >> v;
            if (!restructured[v]) {
                restructured[v] = 1;
                fw.add(tin[v], 1);
            }
        } else {
            int v, k;
            cin >> v >> k;

            int a = nearestRestructuredAncestor(v);
            int distToA = a ? (depth[v] - depth[a]) : depth[v];

            if (k <= distToA) {
                int targetDepth = depth[v] - k;
                int l = 1, r = targetDepth, ansDepth = 0;
                while (l <= r) {
                    int mid = (l + r) >> 1;
                    int anc = kthAncestorOriginal(v, depth[v] - mid);
                    if (fw.rangeSum(tin[anc], tin[v]) > 0) {
                        ansDepth = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                int d = targetDepth;
                int low = ansDepth + 1, high = d, best = d;
                while (low <= high) {
                    int mid = (low + high) >> 1;
                    int anc = kthAncestorOriginal(v, depth[v] - mid);
                    if (fw.rangeSum(tin[anc], tin[v]) == 0) {
                        best = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                cout << kthAncestorOriginal(v, depth[v] - best) << '\n';
            } else {
                int rem = k - distToA;
                int cur = a ? a : 1;
                if (rem == 0) {
                    cout << cur << '\n';
                    continue;
                }
                int targetDepth = depth[cur] - rem;
                int l = 1, r = targetDepth, ansDepth = 0;
                while (l <= r) {
                    int mid = (l + r) >> 1;
                    int anc = kthAncestorOriginal(cur, depth[cur] - mid);
                    if (fw.rangeSum(tin[anc], tin[cur]) > 0) {
                        ansDepth = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                int d = targetDepth;
                int low = ansDepth + 1, high = d, best = d;
                while (low <= high) {
                    int mid = (low + high) >> 1;
                    int anc = kthAncestorOriginal(cur, depth[cur] - mid);
                    if (fw.rangeSum(tin[anc], tin[cur]) == 0) {
                        best = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                cout << kthAncestorOriginal(cur, depth[cur] - best) << '\n';
            }
        }
    }

    return 0;
}
