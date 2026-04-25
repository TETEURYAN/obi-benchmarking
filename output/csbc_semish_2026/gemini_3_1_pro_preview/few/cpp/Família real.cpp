#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <= n; i++) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    vector<bool> attended(n + 1, false);
    for (int i = 0; i < m; i++) {
        int a;
        cin >> a;
        attended[a] = true;
    }

    vector<int> depth(n + 1, 0);
    int max_depth = 0;
    queue<int> q;
    q.push(0);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            depth[v] = depth[u] + 1;
            max_depth = max(max_depth, depth[v]);
            q.push(v);
        }
    }

    vector<int> total_gen(max_depth + 1, 0);
    vector<int> attended_gen(max_depth + 1, 0);

    for (int i = 1; i <= n; i++) {
        int d = depth[i];
        total_gen[d]++;
        if (attended[i]) {
            attended_gen[d]++;
        }
    }

    cout << fixed << setprecision(2);
    for (int d = 1; d <= max_depth; d++) {
        cout << (double)attended_gen[d] / total_gen[d] * 100.0;
        if (d == max_depth) cout << "\n";
        else cout << " ";
    }

    return 0;
}