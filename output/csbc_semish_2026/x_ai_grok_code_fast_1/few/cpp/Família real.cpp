#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<int> pai(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> pai[i];
    }
    vector<vector<int>> filhos(N + 1);
    for (int i = 1; i <= N; i++) {
        filhos[pai[i]].push_back(i);
    }
    vector<int> gen(N + 1, -1);
    gen[0] = 0;
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : filhos[u]) {
            if (gen[v] == -1) {
                gen[v] = gen[u] + 1;
                q.push(v);
            }
        }
    }
    int max_g = 0;
    for (int i = 1; i <= N; i++) {
        max_g = max(max_g, gen[i]);
    }
    vector<int> total(max_g + 1, 0);
    for (int i = 1; i <= N; i++) {
        total[gen[i]]++;
    }
    set<int> attended;
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        attended.insert(x);
    }
    vector<int> attend(max_g + 1, 0);
    for (int i = 1; i <= N; i++) {
        if (attended.count(i)) {
            attend[gen[i]]++;
        }
    }
    cout << fixed << setprecision(2);
    for (int g = 1; g <= max_g; g++) {
        cout << (attend[g] * 100.0 / total[g]);
        if (g < max_g) cout << " ";
        else cout << "\n";
    }
    return 0;
}