
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
vector<vector<int>> adj;
int N;

int dfs(int node, int parent) {
    int count_with_leaf = 0;
    vector<int> child_mins;
    for (int child : adj[node]) {
        if (child == parent) continue;
        int sub_min = dfs(child, node);
        if (sub_min != INF) {
            count_with_leaf++;
            child_mins.push_back(sub_min);
        }
    }
    if (count_with_leaf >= 2) {
        return 2;
    } else if (count_with_leaf == 1) {
        return child_mins[0];
    } else {
        return INF;
    }
}

int main() {
    cin >> N;
    adj.resize(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    if (N == 2) {
        cout << 1 << endl;
        return 0;
    }
    int ans = dfs(1, -1);
    cout << ans << endl;
    return 0;
}
