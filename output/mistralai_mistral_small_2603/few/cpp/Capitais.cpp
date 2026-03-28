#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> degree;
vector<int> leaves;

void find_leaves(int n) {
    for (int i = 1; i <= n; i++) {
        if (degree[i] == 1) {
            leaves.push_back(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    adj.resize(n + 1);
    degree.resize(n + 1, 0);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    find_leaves(n);

    int max_dist = 0;
    queue<pair<int, int>> q;

    for (int leaf : leaves) {
        q.push({leaf, 0});
    }

    vector<bool> visited(n + 1, false);
    while (!q.empty()) {
        auto [node, dist] = q.front();
        q.pop();

        if (visited[node]) continue;
        visited[node] = true;

        if (degree[node] == 1 && node != leaf) {
            max_dist = max(max_dist, dist);
        }

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                q.push({neighbor, dist + 1});
            }
        }
    }

    cout << max_dist << endl;

    return 0;
}