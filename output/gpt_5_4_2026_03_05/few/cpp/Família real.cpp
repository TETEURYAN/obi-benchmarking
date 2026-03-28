#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> parent(N + 1), depth(N + 1, -1);
    for (int i = 1; i <= N; i++) cin >> parent[i];

    depth[0] = 0;
    int maxDepth = 0;

    for (int i = 1; i <= N; i++) {
        if (depth[i] != -1) continue;

        vector<int> path;
        int u = i;
        while (u != 0 && depth[u] == -1) {
            path.push_back(u);
            u = parent[u];
        }

        int d = depth[u];
        for (int j = (int)path.size() - 1; j >= 0; j--) {
            depth[path[j]] = d + 1;
            d++;
            maxDepth = max(maxDepth, depth[path[j]]);
        }
    }

    vector<int> total(maxDepth + 1, 0), present(maxDepth + 1, 0);

    for (int i = 1; i <= N; i++) total[depth[i]]++;

    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        present[depth[x]]++;
    }

    cout << fixed << setprecision(2);
    for (int g = 1; g <= maxDepth; g++) {
        double pct = 100.0 * present[g] / total[g];
        if (g > 1) cout << ' ';
        cout << pct;
    }
    cout << '\n';

    return 0;
}