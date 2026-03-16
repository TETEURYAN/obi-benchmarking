#include <bits/stdc++.h>
using namespace std;

struct SegTree {
    int n;
    vector<int> mx, lazy;

    SegTree() {}
    SegTree(int n_) { init(n_); }

    void init(int n_) {
        n = n_;
        mx.assign(4 * n + 4, 0);
        lazy.assign(4 * n + 4, 0);
    }

    void build(int node, int l, int r, const vector<int>& base) {
        if (l == r) {
            mx[node] = base[l];
            return;
        }
        int mid = (l + r) >> 1;
        build(node << 1, l, mid, base);
        build(node << 1 | 1, mid + 1, r, base);
        mx[node] = max(mx[node << 1], mx[node << 1 | 1]);
    }

    void apply(int node, int val) {
        mx[node] = max(mx[node], val);
        lazy[node] = max(lazy[node], val);
    }

    void push(int node) {
        if (lazy[node]) {
            apply(node << 1, lazy[node]);
            apply(node << 1 | 1, lazy[node]);
            lazy[node] = 0;
        }
    }

    void range_chmax(int node, int l, int r, int ql, int qr, int val) {
        if (ql > r || qr < l || mx[node] >= val) return;
        if (ql <= l && r <= qr) {
            apply(node, val);
            return;
        }
        push(node);
        int mid = (l + r) >> 1;
        if (ql <= mid) range_chmax(node << 1, l, mid, ql, qr, val);
        if (qr > mid) range_chmax(node << 1 | 1, mid + 1, r, ql, qr, val);
        mx[node] = min(max(mx[node << 1], mx[node << 1 | 1]), max(mx[node << 1], mx[node << 1 | 1]));
        mx[node] = max(mx[node << 1], mx[node << 1 | 1]);
    }

    int point_query(int node, int l, int r, int pos) {
        if (l == r) return mx[node];
        push(node);
        int mid = (l + r) >> 1;
        if (pos <= mid) return point_query(node << 1, l, mid, pos);
        return point_query(node << 1 | 1, mid + 1, r, pos);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> p(N + 1, 0);
    vector<vector<int>> children(N + 1);
    for (int i = 2; i <= N; i++) {
        cin >> p[i];
        children[p[i]].push_back(i);
    }

    vector<int> tin(N + 1), tout(N + 1), depth(N + 1), euler(N + 1), parent(N + 1);
    int timer = 0;

    vector<int> st;
    st.push_back(1);
    vector<int> it(N + 1, 0);
    parent[1] = 0;
    depth[1] = 0;

    while (!st.empty()) {
        int u = st.back();
        if (it[u] == 0) {
            tin[u] = ++timer;
            euler[timer] = u;
        }
        if (it[u] < (int)children[u].size()) {
            int v = children[u][it[u]++];
            parent[v] = u;
            depth[v] = depth[u] + 1;
            st.push_back(v);
        } else {
            tout[u] = timer;
            st.pop_back();
        }
    }

    int LOG = 1;
    while ((1 << LOG) <= N) LOG++;
    vector<vector<int>> up(LOG, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; i++) up[0][i] = parent[i];
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= N; i++) {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    auto kth_ancestor_original = [&](int v, int k) {
        for (int j = 0; j < LOG; j++) {
            if (k & (1 << j)) v = up[j][v];
        }
        return v;
    };

    vector<int> base(N + 1);
    for (int i = 1; i <= N; i++) base[tin[i]] = depth[i];

    SegTree seg(N);
    seg.build(1, 1, N, base);

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            int dcur = seg.point_query(1, 1, N, tin[v]);
            int targetDepth = dcur - k;
            int anc = kth_ancestor_original(v, depth[v] - targetDepth);
            cout << anc << '\n';
        } else {
            int v;
            cin >> v;
            seg.range_chmax(1, 1, N, tin[v], tout[v], depth[v] + 1);
        }
    }

    return 0;
}