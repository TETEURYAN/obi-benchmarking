#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> parent(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> parent[i];
    }

    vector<bool> presente(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        presente[x] = true;
    }

    vector<vector<int>> children(N + 1);
    for (int i = 1; i <= N; i++) {
        children[parent[i]].push_back(i);
    }

    vector<int> gen(N + 1, -1);
    queue<int> q;
    gen[0] = 0;
    q.push(0);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : children[u]) {
            if (gen[v] == -1) {
                gen[v] = gen[u] + 1;
                q.push(v);
            }
        }
    }

    int max_gen = 0;
    for (int i = 1; i <= N; i++) {
        if (gen[i] > max_gen) max_gen = gen[i];
    }

    vector<int> total(max_gen + 1, 0);
    vector<int> presente_count(max_gen + 1, 0);
    for (int i = 1; i <= N; i++) {
        int g = gen[i];
        total[g]++;
        if (presente[i]) presente_count[g]++;
    }

    cout << fixed << setprecision(2);
    for (int g = 1; g <= max_gen; g++) {
        double perc = (presente_count[g] * 100.0) / total[g];
        cout << perc;
        if (g < max_gen) cout << " ";
    }
    cout << endl;

    return 0;
}