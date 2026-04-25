#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    vector<int> dist(n + 1, -1);
    vector<int> root(n + 1, -1);
    queue<int> q;

    for (int i = 1; i <= n; ++i) {
        if (deg[i] == 1) {
            dist[i] = 0;
            root[i] = i;
            q.push(i);
        }
    }

    int min_dist = 1e9;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                root[v] = root[u];
                q.push(v);
            } else if (root[v] != root[u]) {
                min_dist = min(min_dist, dist[u] + dist[v] + 1);
            }
        }
    }

    cout << min_dist << "\n";

    return 0;
}