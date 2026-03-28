#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> parent(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> parent[i];
    }

    vector<bool> present(N + 1, false);
    for (int i = 0; i < M; ++i) {
        int p;
        cin >> p;
        present[p] = true;
    }

    vector<int> depth(N + 1, -1);
    depth[0] = 0;
    function<int(int)> getDepth = [&](int node) -> int {
        if (depth[node] != -1) return depth[node];
        return depth[node] = getDepth(parent[node]) + 1;
    };

    int maxDepth = 0;
    for (int i = 1; i <= N; ++i) {
        int d = getDepth(i);
        maxDepth = max(maxDepth, d);
    }

    vector<int> total(maxDepth + 1, 0);
    vector<int> attended(maxDepth + 1, 0);

    for (int i = 1; i <= N; ++i) {
        int d = depth[i];
        total[d]++;
        if (present[i]) attended[d]++;
    }

    cout << fixed << setprecision(2);
    for (int g = 1; g <= maxDepth; ++g) {
        double perc = (total[g] == 0) ? 0.0 : (100.0 * attended[g] / total[g]);
        cout << perc;
        if (g < maxDepth) cout << " ";
    }
    cout << endl;

    return 0;
}