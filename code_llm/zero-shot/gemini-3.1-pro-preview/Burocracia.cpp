#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 100005;
int n;
pair<int, int> tree[2 * MAXN];

void update(int l, int r, pair<int, int> val) {
    for (l += n, r += n + 1; l < r; l >>= 1, r >>= 1) {
        if (l & 1) {
            tree[l] = min(tree[l], val);
            l++;
        }
        if (r & 1) {
            r--;
            tree[r] = min(tree[r], val);
        }
    }
}

pair<int, int> query(int p) {
    pair<int, int> res = {1e9, -1};
    for (p += n; p > 0; p >>= 1) {
        res = min(res, tree[p]);
    }
    return res;
}

int timer = 0;
int in_time[MAXN], out_time[MAXN], depth[MAXN];
int up[MAXN][20];
vector<int> adj[MAXN];

void dfs(int u, int p, int d) {
    in_time[u] = timer++;
    depth[u] = d;
    up[u][0] = p;
    for (int i = 1; i < 20; i++) {
        up[u][i] = up[up[u][i-1]][i-1];
    }
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
    out_time[u] = timer - 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    for (int i = 2; i <= N; i++) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1, 1, 0);

    n = N;
    for (int i = 0; i < 2 * n; i++) {
        tree[i] = {1e9, -1};
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, k;
            cin >> v >> k;
            int p_orig = up[v][0];
            pair<int, int> res = query(in_time[p_orig]);
            int w1 = (res.first == 1e9) ? p_orig : res.second;
            int ans = w1;
            k--;
            for (int i = 0; i < 20; i++) {
                if ((k >> i) & 1) {
                    ans = up[ans][i];
                }
            }
            cout << ans << "\n";
        } else if (type == 2) {
            int v;
            cin >> v;
            update(in_time[v], out_time[v], {depth[v], v});
        }
    }

    return 0;
}