#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    vector<int> deg(N + 1, 0);

    for (int i = 0; i < N - 1; i++) {
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

    vector<int> dist(N + 1, -1), src(N + 1, 0);
    queue<int> q;

    for (int i = 1; i <= N; i++) {
        if (deg[i] == 1) {
            dist[i] = 0;
            src[i] = i;
            q.push(i);
        }
    }

    int ans = INT_MAX;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                src[v] = src[u];
                q.push(v);
            } else if (src[v] != src[u]) {
                ans = min(ans, dist[u] + dist[v] + 1);
            }
        }
    }

    cout << ans << '\n';
    return 0;
}