
#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M;
    cin >> N >> M;
    
    vector<int> parent(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> parent[i];
    }
    
    vector<vector<int>> children(N + 1);
    for (int i = 1; i <= N; i++) {
        children[parent[i]].push_back(i);
    }
    
    vector<bool> attended(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        attended[x] = true;
    }
    
    vector<int> gen(N + 1, -1);
    queue<int> q;
    gen[0] = 0;
    q.push(0);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : children[u]) {
            gen[v] = gen[u] + 1;
            q.push(v);
        }
    }
    
    int maxGen = 0;
    for (int i = 1; i <= N; i++) {
        if (gen[i] > maxGen) maxGen = gen[i];
    }
    
    vector<int> total(maxGen + 1, 0);
    vector<int> present(maxGen + 1, 0);
    for (int i = 1; i <= N; i++) {
        int g = gen[i];
        total[g]++;
        if (attended[i]) present[g]++;
    }
    
    cout << fixed << setprecision(2);
    for (int g = 1; g <= maxGen; g++) {
        if (g > 1) cout << " ";
        double perc = (present[g] * 100.0) / total[g];
        cout << perc;
    }
    cout << endl;
    
    return 0;
}
