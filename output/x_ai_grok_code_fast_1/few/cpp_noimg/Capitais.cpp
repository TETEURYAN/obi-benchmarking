#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
    vector<int> leaves;
    for (int i = 1; i <= n; i++) {
        if (deg[i] == 1) leaves.push_back(i);
    }
    vector<int> leaf_count(n + 1, 0);
    for (int u = 1; u <= n; u++) {
        for (int v : adj[u]) {
            if (deg[v] == 1) leaf_count[u]++;
        }
    }
    bool has_two = false;
    for (int i = 1; i <= n; i++) {
        if (leaf_count[i] >= 2) has_two = true;
    }
    if (has_two) {
        cout << 2 << endl;
        return 0;
    }
    // find diameter
    auto bfs = [&](int start) -> pair<int, vector<int>> {
        vector<int> dist(n + 1, -1);
        vector<int> parent(n + 1, -1);
        queue<int> q;
        q.push(start);
        dist[start] = 0;
        int farthest = start;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                    if (dist[v] > dist[farthest]) farthest = v;
                }
            }
        }
        return {farthest, parent};
    };
    auto [end1, _] = bfs(leaves[0]);
    auto [end2, parent] = bfs(end1);
    // reconstruct path
    vector<int> path;
    int current = end2;
    while (current != -1) {
        path.push_back(current);
        current = parent[current];
    }
    reverse(path.begin(), path.end());
    // find leaf positions
    vector<int> leaf_pos;
    for (int i = 0; i < path.size(); i++) {
        if (deg[path[i]] == 1) leaf_pos.push_back(i);
    }
    int min_d = INT_MAX;
    for (size_t i = 1; i < leaf_pos.size(); i++) {
        min_d = min(min_d, leaf_pos[i] - leaf_pos[i - 1]);
    }
    cout << min_d << endl;
    return 0;
}