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

    vector<bool> present(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        present[x] = true;
    }

    vector<vector<int>> generations;
    generations.push_back({0});

    vector<int> current_gen = {0};
    while (!current_gen.empty()) {
        vector<int> next_gen;
        for (int person : current_gen) {
            for (int i = 1; i <= N; i++) {
                if (parent[i] == person && !present[i]) {
                    next_gen.push_back(i);
                }
            }
        }
        if (!next_gen.empty()) {
            generations.push_back(next_gen);
        }
        current_gen = next_gen;
    }

    vector<int> gen_counts;
    vector<int> present_counts;

    for (int i = 0; i < generations.size(); i++) {
        int total = generations[i].size();
        int count = 0;
        for (int person : generations[i]) {
            if (present[person]) {
                count++;
            }
        }
        gen_counts.push_back(total);
        present_counts.push_back(count);
    }

    for (int i = 0; i < gen_counts.size(); i++) {
        double percentage = (gen_counts[i] == 0) ? 0.0 : (100.0 * present_counts[i] / gen_counts[i]);
        cout << fixed << setprecision(2) << percentage;
        if (i < gen_counts.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}