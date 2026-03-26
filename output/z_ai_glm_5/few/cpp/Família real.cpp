
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 10005;

int parent[MAXN];
int generation[MAXN];
int total_per_gen[MAXN];
int attend_per_gen[MAXN];

int find_generation(int u) {
    if (u == 0) return 0;
    if (generation[u] != -1) return generation[u];
    return generation[u] = find_generation(parent[u]) + 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 1; i <= n; i++) {
        cin >> parent[i];
    }

    memset(generation, -1, sizeof(generation));
    generation[0] = 0;
    
    int max_gen = 0;

    for (int i = 1; i <= n; i++) {
        int gen = find_generation(i);
        total_per_gen[gen]++;
        if (gen > max_gen) {
            max_gen = gen;
        }
    }

    for (int i = 0; i < m; i++) {
        int u;
        cin >> u;
        int gen = find_generation(u);
        attend_per_gen[gen]++;
    }

    cout << fixed << setprecision(2);

    for (int g = 1; g <= max_gen; g++) {
        double perc = 0.0;
        if (total_per_gen[g] > 0) {
            perc = (double)attend_per_gen[g] * 100.0 / total_per_gen[g];
        }
        if (g > 1) cout << " ";
        cout << perc;
    }
    cout << endl;

    return 0;
}
