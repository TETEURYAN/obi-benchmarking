
#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 100005;
const int INF = 1e9;

int N, Q;
int p[MAXN];
vector<int> adj[MAXN];

int up[MAXN][20];
int depth[MAXN];
int in[MAXN], out[MAXN];
int timer = 0;

int tree[4 * MAXN];

void dfs(int u, int p_node, int d) {
    in[u] = ++timer;
    depth[u] = d;
    up[u][0] = p_node;
    for (int i = 1; i < 20; i++) {
        up[u][i] = up[up[u][i-1]][i-1];
    }
    for (int v : adj[u]) {
        if (v != p_node) {
            dfs(v, u, d + 1);
        }
    }
    out[u] = timer;
}

void update(int node, int l, int r, int ql, int qr, int u) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        if (depth[u] < depth[tree[node]]) {
            tree[node] = u;
        }
        return;
    }
    int mid = (l + r) / 2;
    update(2 * node, l, mid, ql, qr, u);
    update(2 * node + 1, mid + 1, r, ql, qr, u);
}

int query(int node, int l, int r, int pos) {
    int res = tree[node];
    if (l == r) return res;
    int mid = (l + r) / 2;
    int child_res;
    if (pos <= mid) {
        child_res = query(2 * node, l, mid, pos);
    } else {
        child_res = query(2 * node + 1, mid + 1, r, pos);
    }
    if (depth[child_res] < depth[res]) {
        res = child_res;
    }
    return res;
}

int get_kth_ancestor(int u, int k) {
    for (int j = 0; j < 20; j++) {
        if (k & (1 << j)) {
            u = up[u][j];
        }
    }
    return u;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    for (int i = 2; i <= N; i++) {
        cin >> p[i];
        adj[p[i]].push_back(i);
    }

    depth[0] = INF;
    dfs(1, 1, 0);

    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            int h = query(1, 1, N, in[v]);
            if (h == 0) {
                cout << get_kth_ancestor(v, k) << "\n";
            } else {
                if (k == 1) {
                    cout << h << "\n";
                } else {
                    cout << get_kth_ancestor(h, k - 1) << "\n";
                }
            }
        } else {
            int v;
            cin >> v;
            if (in[v] + 1 <= out[v]) {
                update(1, 1, N, in[v] + 1, out[v], v);
            }
        }
    }

    return 0;
}
