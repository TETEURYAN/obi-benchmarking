#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> adj(n + 1);
    vector<int> degree(n + 1, 0);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    queue<int> q;
    vector<int> dist(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        if (degree[i] == 1) {
            q.push(i);
            dist[i] = 1;
        }
    }

    int remaining = n;
    while (remaining > 2) {
        int sz = q.size();
        remaining -= sz;
        for (int i = 0; i < sz; i++) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (--degree[v] == 1) {
                    q.push(v);
                    dist[v] = dist[u] + 1;
                }
            }
        }
    }

    int ans = n;
    for (int i = 1; i <= n; i++) {
        if (degree[i] == 1) {
            ans = min(ans, dist[i]);
        }
    }

    cout << ans << '\n';
    return 0;
}