
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> pais(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> pais[i];
    }
    vector<vector<int>> filhos(N + 1);
    for (int i = 1; i <= N; i++) {
        filhos[pais[i]].push_back(i);
    }
    vector<int> depth(N + 1, -1);
    queue<int> q;
    q.push(0);
    depth[0] = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : filhos[u]) {
            if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                q.push(v);
            }
        }
    }
    vector<bool> presente(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        presente[x] = true;
    }
    int maxd = 0;
    for (int i = 1; i <= N; i++) {
        maxd = max(maxd, depth[i]);
    }
    vector<int> total(maxd + 1, 0);
    vector<int> pres(maxd + 1, 0);
    for (int i = 1; i <= N; i++) {
        int d = depth[i];
        total[d]++;
        if (presente[i]) pres[d]++;
    }
    cout << fixed << setprecision(2);
    for (int g = 1; g <= maxd; g++) {
        double perc = (double)pres[g] / total[g] * 100.0;
        cout << perc;
        if (g < maxd) cout << " ";
        else cout << endl;
    }
    return 0;
}
