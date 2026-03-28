#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<int> parent(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> parent[i];
    }

    vector<bool> attended(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        attended[x] = true;
    }

    // BFS to find depth of each node
    // King is node 0, depth 0
    // Children of king are depth 1, etc.
    vector<int> depth(N + 1, -1);
    for (int i = 1; i <= N; i++) {
        // compute depth by following parent chain
        // but we need to do it efficiently
        // since N <= 10000, we can do it with memoization
    }

    // Use iterative depth computation with memoization
    function<int(int)> getDepth = [&](int node) -> int {
        if (node == 0) return 0;
        if (depth[node] != -1) return depth[node];
        depth[node] = getDepth(parent[node]) + 1;
        return depth[node];
    };

    for (int i = 1; i <= N; i++) {
        getDepth(i);
    }

    // Find max depth
    int maxDepth = 0;
    for (int i = 1; i <= N; i++) {
        maxDepth = max(maxDepth, depth[i]);
    }

    // For each generation (depth 1 to maxDepth), count total and attended
    vector<int> total(maxDepth + 1, 0);
    vector<int> present(maxDepth + 1, 0);

    for (int i = 1; i <= N; i++) {
        int d = depth[i];
        total[d]++;
        if (attended[i]) present[d]++;
    }

    // Output percentages for depth 1 to maxDepth
    cout << fixed << setprecision(2);
    for (int d = 1; d <= maxDepth; d++) {
        double pct = 0.0;
        if (total[d] > 0) {
            pct = 100.0 * present[d] / total[d];
        }
        if (d > 1) cout << " ";
        cout << pct;
    }
    cout << endl;

    return 0;
}