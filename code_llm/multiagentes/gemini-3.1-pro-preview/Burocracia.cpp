#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 100005;
const int LOG = 18;

int N, Q;
vector<int> adj[MAXN];
int up[MAXN][LOG];
int orig_depth[MAXN];
int in[MAXN], out[MAXN], rev_in[MAXN];
int head[MAXN];
int lazy_tree[4 * MAXN];

void build(int node, int l, int r) {
    if (l == r) {
        lazy_tree[node] = orig_depth[rev_in[l]];
        return;
    }
    lazy_tree[node] = -1;
    int mid = l + (r - l) / 2;
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
}

void update(int node, int l, int r, int ql, int qr, int val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) {
        lazy_tree[node] = val;
        return;
    }
    if (lazy_tree[node] != -1) {
        lazy_tree[2 * node] = lazy_tree[node];
        lazy_tree[2 * node + 1] = lazy_tree[node];
        lazy_tree[node] = -1;
    }
    int mid = l + (r - l) / 2;
    update(2 * node, l, mid, ql, qr, val);
    update(2 * node + 1, mid + 1, r, ql, qr, val);
}

int query(int node, int l, int r, int pos) {
    if (lazy_tree[node] != -1) return lazy_tree[node];
    int mid = l + (r - l) / 2;
    if (pos <= mid) return query(2 * node, l, mid, pos);
    else return query(2 * node + 1, mid + 1, r, pos);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    orig_depth[1] = 0;
    up[1][0] = 0;
    for (int i = 2; i <= N; i++) {
        int p;
        cin >> p;
        adj[p].push_back(i);
        orig_depth[i] = orig_depth[p] + 1;
        up[i][0] = p;
    }

    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= N; i++) {
            up[i][j] = up[up[i][j - 1]][j - 1];
        }
    }

    int timer = 0;
    vector<int> stk;
    stk.push_back(1);
    in[1] = ++timer;
    rev_in[timer] = 1;

    while (!stk.empty()) {
        int u = stk.back();
        if (head[u] < (int)adj[u].size()) {
            int v = adj[u][head[u]++];
            in[v] = ++timer;
            rev_in[timer] = v;
            stk.push_back(v);
        } else {
            out[u] = timer;
            stk.pop_back();
        }
    }

    build(1, 1, N);

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, k;
            cin >> u >> k;
            int target_depth = query(1, 1, N, in[u]) - k;
            for (int j = LOG - 1; j >= 0; j--) {
                int nxt = up[u][j];
                if (nxt != 0) {
                    int d = query(1, 1, N, in[nxt]);
                    if (d > target_depth) {
                        u = nxt;
                    }
                }
            }
            cout << up[u][0] << "\n";
        } else if (type == 2) {
            int v;
            cin >> v;
            int curr_depth = query(1, 1, N, in[v]);
            if (in[v] + 1 <= out[v]) {
                update(1, 1, N, in[v] + 1, out[v], curr_depth + 1);
            }
        }
    }

    return 0;
}