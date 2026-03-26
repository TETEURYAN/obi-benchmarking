#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<vector<int>> adj(N + 1);
    vector<int> grau(N + 1, 0);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        grau[u]++;
        grau[v]++;
    }

    int raiz = 1;
    vector<int> pai(N + 1, -1);
    vector<int> order;
    queue<int> q;
    q.push(raiz);
    pai[raiz] = 0;
    while (!q.empty()) {
        int v = q.front(); q.pop();
        order.push_back(v);
        for (int u : adj[v]) {
            if (u == pai[v]) continue;
            pai[u] = v;
            q.push(u);
        }
    }

    const int INF = 1e9;
    vector<int> minDist(N + 1, -1);
    for (int i = (int)order.size() - 1; i >= 0; i--) {
        int v = order[i];
        if (grau[v] == 1) {
            minDist[v] = 0;
        } else {
            minDist[v] = INF;
            for (int u : adj[v]) {
                if (u == pai[v]) continue;
                minDist[v] = min(minDist[v], 1 + minDist[u]);
            }
        }
    }

    long long ans = LLONG_MAX;
    for (int v = 1; v <= N; v++) {
        vector<int> dists;
        if (grau[v] == 1) {
            dists.push_back(0);
        }
        for (int u : adj[v]) {
            if (u == pai[v]) continue;
            dists.push_back(1 + minDist[u]);
        }
        if (dists.size() >= 2) {
            sort(dists.begin(), dists.end());
            ans = min(ans, (long long)dists[0] + dists[1]);
        }
    }

    cout << ans << endl;

    return 0;
}