
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 100005;
int up[17][MAXN];
vector<int> adj[MAXN];
int in[MAXN], out[MAXN], depth[MAXN];
int timer = 0;
pair<int, int> tree[4 * MAXN];

void dfs(int u, int d) {
    in[u] = ++timer;
    depth[u] = d;
    for (int v : adj[u]) {
        dfs(v, d + 1);
    }
    out[u] = timer;
}

void build(int node, int l, int r) {
    tree[node] = {1e9, -1};
    if (l == r) return;
    int mid = l + (r - l) / 2;
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
}

void update(int node, int l, int r, int ql, int qr, pair<int, int> val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        tree[node] = min(tree[node], val);
        return;
    }
    int mid = l + (r - l) / 2;
    update(2 * node, l, mid, ql, qr, val);
    update(2 * node + 1, mid + 1, r, ql, qr, val);
}

pair<int, int> query(int node, int l, int r, int pos) {
    if (l == r) return tree[node];
    int mid = l + (r - l) / 2;
    pair<int, int> res = tree[node];
    if (pos <= mid) {
        res = min(res, query(2 * node, l, mid, pos));
    } else {
        res = min(res, query(2 * node + 1, mid + 1, r, pos));
    }
    return res;
}

int get_kth_ancestor(int u, int k) {
    for (int i = 0; i < 17; ++i) {
        if ((k >> i) & 1) {
            u = up[i][u];
        }
    }
    return u;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    for (int i = 2; i <= N; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
        up[0][i] = p;
    }
    up[0][1] = 0;

    dfs(1, 0);

    for (int i = 1; i < 17; ++i) {
        for (int j = 1; j <= N; ++j) {
            up[i][j] = up[i-1][up[i-1][j]];
        }
    }

    build(1, 1, N);

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            pair<int, int> h = query(1, 1, N, in[v]);
            if (h.first != 1e9) {
                int highest_ancestor = h.second;
                cout << get_kth_ancestor(highest_ancestor, k - 1) << "\n";
            } else {
                cout << get_kth_ancestor(v, k) << "\n";
            }
        } else {
            int v;
            cin >> v;
            if (in[v] + 1 <= out[v]) {
                update(1, 1, N, in[v] + 1, out[v], {depth[v], v});
            }
        }
    }

    return 0;
}
