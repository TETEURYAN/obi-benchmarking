
#include <iostream>
#include <vector>
#include <map>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> parents(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> parents[i];
    }

    vector<bool> present(N + 1, false);
    for (int i = 0; i < M; ++i) {
        int num;
        cin >> num;
        present[num] = true;
    }

    map<int, vector<int>> generations;
    for (int i = 1; i <= N; ++i) {
        int current = i;
        int generation = 0;
        while (parents[current] != 0) {
            current = parents[current];
            generation++;
        }
        generations[generation].push_back(i);
    }

    vector<int> generation_counts;
    vector<int> present_counts;
    for (const auto& gen : generations) {
        generation_counts.push_back(gen.second.size());
        int count = 0;
        for (int person : gen.second) {
            if (present[person]) {
                count++;
            }
        }
        present_counts.push_back(count);
    }

    for (int i = 0; i < generation_counts.size(); ++i) {
        double percentage = (generation_counts[i] == 0) ? 0.0 : (100.0 * present_counts[i] / generation_counts[i]);
        cout << fixed << setprecision(2) << percentage;
        if (i < generation_counts.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
