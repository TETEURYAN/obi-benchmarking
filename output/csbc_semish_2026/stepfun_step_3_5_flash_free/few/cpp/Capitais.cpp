#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;
    vector<vector<int>> adj(N + 1);
    vector<int> degree(N + 1, 0);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    if (N == 2) {
        cout << 1 << '\n';
        return 0;
    }

    vector<int> capitals;
    for (int i = 1; i <= N; i++) {
        if (degree[i] == 1) {
            capitals.push_back(i);
        }
    }

    vector<int> count_parent(N + 1, 0);
    for (int c : capitals) {
        int v = adj[c][0];
        count_parent[v]++;
    }

    for (int i = 1; i <= N; i++) {
        if (count_parent[i] >= 2) {
            cout << 2 << '\n';
            return 0;
        }
    }

    vector<int> sources;
    for (int c : capitals) {
        int v = adj[c][0];
        sources.push_back(v);
    }

    vector<int> dist(N + 1, -1);
    vector<int> src(N + 1, -1);
    queue<int> q;
    for (int v : sources) {
        dist[v] = 0;
        src[v] = v;
        q.push(v);
    }

    int min_dist = INT_MAX;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int w : adj[u]) {
            if (dist[w] == -1) {
                dist[w] = dist[u] + 1;
                src[w] = src[u];
                q.push(w);
            } else if (src[w] != src[u]) {
                int candidate = dist[u] + 1 + dist[w];
                if (candidate < min_dist) min_dist = candidate;
            }
        }
    }

    cout << 2 + min_dist << '\n';

    return 0;
}