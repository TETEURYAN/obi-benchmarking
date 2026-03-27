
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<vector<int>> adj;
vector<int> degree;

int bfs(int start) {
    vector<int> dist(adj.size(), -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);
    int farthest = start;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
                if (dist[v] > dist[farthest]) {
                    farthest = v;
                }
            }
        }
    }
    return farthest;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    adj.resize(N + 1);
    degree.resize(N + 1, 0);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    vector<int> leaves;
    for (int i = 1; i <= N; ++i) {
        if (degree[i] == 1) {
            leaves.push_back(i);
        }
    }

    if (leaves.size() == 2) {
        int u = leaves[0];
        int v = leaves[1];
        int a = bfs(u);
        int b = bfs(a);
        cout << (dist[b] + 1) / 2 << '\n';
    } else {
        int u = leaves[0];
        int a = bfs(u);
        int b = bfs(a);
        int diameter = dist[b];
        cout << (diameter + 1) / 2 << '\n';
    }

    return 0;
}
