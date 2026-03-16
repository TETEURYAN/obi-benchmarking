#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick() {}
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
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
    if (!(cin >> N)) return 0;

    vector<int> parent(N + 1, 0);
    vector<vector<int>> children(N + 1);
    parent[1] = 0;
    for (int i = 2; i <= N; i++) {
        cin >> parent[i];
        children[parent[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1);
    vector<vector<int>> up(18, vector<int>(N + 1, 0));
    int timer = 0;

    vector<pair<int,int>> st;
    st.reserve(2 * N);
    st.push_back({1, 0});
    depth[1] = 0;
    up[0][1] = 0;

    while (!st.empty()) {
        auto [v, state] = st.back();
        st.pop_back();
        if (state == 0) {
            tin[v] = ++timer;
            st.push_back({v, 1});
            for (int i = (int)children[v].size() - 1; i >= 0; i--) {
                int u = children[v][i];
                depth[u] = depth[v] + 1;
                up[0][u] = v;
                for (int j = 1; j < 18; j++) up[j][u] = up[j - 1][up[j - 1][u]];
                st.push_back({u, 0});
            }
        } else {
            tout[v] = timer;
        }
    }

    auto isAncestor = [&](int a, int b) -> bool {
        return tin[a] <= tin[b] && tout[b] <= tout[a];
    };

    auto lca = [&](int a, int b) -> int {
        if (isAncestor(a, b)) return a;
        if (isAncestor(b, a)) return b;
        for (int j = 17; j >= 0; j--) {
            int x = up[j][a];
            if (x != 0 && !isAncestor(x, b)) a = x;
        }
        return up[0][a];
    };

    auto kthAncestorOriginal = [&](int v, int k) -> int {
        for (int j = 0; j < 18; j++) {
            if (k & (1 << j)) v = up[j][v];
        }
        return v;
    };

    int Q;
    cin >> Q;

    Fenwick bit(N + 2);
    vector<int> marked(N + 1, 0);

    auto activeCountOnPath = [&](int v) -> int {
        return bit.sumPrefix(tin[v]);
    };

    auto nearestActiveAncestor = [&](int v) -> int {
        if (activeCountOnPath(v) == 0) return 1;
        int cur = v;
        for (int j = 17; j >= 0; j--) {
            int x = up[j][cur];
            if (x != 0 && activeCountOnPath(x) > 0) cur = x;
        }
        return cur;
    };

    auto compressedParent = [&](int v) -> int {
        if (v == 1) return 0;
        int a = nearestActiveAncestor(v);
        if (a == 1 && !marked[1]) return 1;
        return a;
    };

    auto jumpCompressed = [&](int v, int k) -> int {
        while (k > 0) {
            int a = nearestActiveAncestor(v);
            int d = depth[v] - depth[a];
            if (d >= k) return kthAncestorOriginal(v, k);
            k -= d;
            v = a;
            if (k == 0) return v;
            if (v == 1) return 1;
            v = parent[a];
            k--;
        }
        return v;
    };

    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            cout << jumpCompressed(v, k) << '\n';
        } else {
            int v;
            cin >> v;
            if (!marked[v]) {
                marked[v] = 1;
                bit.add(tin[v], 1);
                bit.add(tout[v] + 1, -1);
            }
        }
    }

    return 0;
}