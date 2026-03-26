#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> adj(N + 1);
    vector<int> deg(N + 1, 0);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    if (N == 2) {
        cout << 1 << '\n';
        return 0;
    }

    const int INF = 1e9;
    vector<int> dist(N + 1, INF);
    queue<int> q;

    for (int i = 1; i <= N; ++i) {
        if (deg[i] == 1) {
            dist[i] = 0;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == INF) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    int ans = INF;
    for (int u = 1; u <= N; ++u) {
        if (deg[u] == 1) {
            for (int v : adj[u]) {
                if (deg[v] > 1) {
                    ans = min(ans, dist[v] + 1);
                }
            }
        }
    }

    cout << ans << '\n';
    return 0;
}