
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> degree(n + 1, 0);
    vector<pair<int, int>> edges;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
        edges.push_back({u, v});
    }

    vector<int> dist(n + 1, -1);
    vector<int> source(n + 1, -1);
    queue<int> q;

    for (int i = 1; i <= n; ++i) {
        if (degree[i] == 1) {
            dist[i] = 0;
            source[i] = i;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                source[v] = source[u];
                q.push(v);
            }
        }
    }

    int min_dist = INT_MAX;

    for (const auto& edge : edges) {
        int u = edge.first;
        int v = edge.second;
        if (source[u] != source[v]) {
            int d = dist[u] + dist[v] + 1;
            if (d < min_dist) {
                min_dist = d;
            }
        }
    }

    cout << min_dist << endl;

    return 0;
}
