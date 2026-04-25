
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    if (N == 2) {
        int u, v;
        cin >> u >> v;
        cout << 1 << '\n';
        return 0;
    }
    
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
    
    vector<bool> isLeaf(N + 1, false);
    for (int i = 1; i <= N; i++) {
        if (grau[i] == 1) isLeaf[i] = true;
    }
    
    for (int i = 1; i <= N; i++) {
        int count = 0;
        for (int v : adj[i]) {
            if (isLeaf[v]) count++;
        }
        if (count >= 2) {
            cout << 2 << '\n';
            return 0;
        }
    }
    
    vector<int> P;
    for (int i = 1; i <= N; i++) {
        if (isLeaf[i]) {
            P.push_back(adj[i][0]);
        }
    }
    
    vector<int> dist(N + 1, -1);
    vector<int> source(N + 1, -1);
    queue<int> q;
    for (int v : P) {
        dist[v] = 0;
        source[v] = v;
        q.push(v);
    }
    
    int minDist = INT_MAX;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int w : adj[u]) {
            if (dist[w] == -1) {
                dist[w] = dist[u] + 1;
                source[w] = source[u];
                q.push(w);
            } else if (source[w] != source[u]) {
                int candidate = dist[w] + dist[u] + 1;
                if (candidate < minDist) minDist = candidate;
            }
        }
    }
    
    cout << 2 + minDist << '\n';
    
    return 0;
}
