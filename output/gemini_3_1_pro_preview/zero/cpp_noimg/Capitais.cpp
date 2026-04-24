
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;
int n;
vector<vector<int>> adj;
int ans = INF;

int dfs(int u, int p) {
    int m1 = INF, m2 = INF;
    bool is_leaf = true;
    for (int v : adj[u]) {
        if (v == p) continue;
        is_leaf = false;
        int d = dfs(v, u) + 1;
        if (d < m1) {
            m2 = m1;
            m1 = d;
        } else if (d < m2) {
            m2 = d;
        }
    }
    if (is_leaf) return 0;
    if (m2 != INF) {
        ans = min(ans, m1 + m2);
    }
    return m1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    if (!(cin >> n)) return 0;
    
    if (n == 2) {
        cout << 1 << "\n";
        return 0;
    }
    
    adj.resize(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    int root = 1;
    for (int i = 1; i <= n; ++i) {
        if (adj[i].size() > 1) {
            root = i;
            break;
        }
    }
    
    dfs(root, 0);
    
    cout << ans << "\n";
    
    return 0;
}
