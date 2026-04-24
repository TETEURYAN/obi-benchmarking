#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> parent(N + 1), gen(N + 1, -1);
    for (int i = 1; i <= N; i++) cin >> parent[i];

    function<int(int)> getGen = [&](int u) -> int {
        if (u == 0) return 0;
        if (gen[u] != -1) return gen[u];
        return gen[u] = getGen(parent[u]) + 1;
    };

    int maxGen = 0;
    vector<int> total(N + 1, 0), present(N + 1, 0);

    for (int i = 1; i <= N; i++) {
        int g = getGen(i);
        total[g]++;
        maxGen = max(maxGen, g);
    }

    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        present[getGen(x)]++;
    }

    cout << fixed << setprecision(2);
    for (int g = 1; g <= maxGen; g++) {
        if (g > 1) cout << ' ';
        double pct = 100.0 * present[g] / total[g];
        cout << pct;
    }
    cout << '\n';

    return 0;
}