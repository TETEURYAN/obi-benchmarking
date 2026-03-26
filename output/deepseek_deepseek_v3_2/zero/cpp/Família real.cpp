
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> parent(N + 1);
    parent[0] = -1;

    for (int i = 1; i <= N; i++) {
        int p;
        cin >> p;
        parent[i] = p;
    }

    vector<bool> attended(N + 1, false);
    for (int i = 0; i < M; i++) {
        int id;
        cin >> id;
        attended[id] = true;
    }

    vector<int> generation(N + 1, 0);
    generation[0] = 0;

    for (int i = 1; i <= N; i++) {
        generation[i] = generation[parent[i]] + 1;
    }

    vector<int> total_in_gen(10001, 0);
    vector<int> attended_in_gen(10001, 0);

    for (int i = 1; i <= N; i++) {
        int gen = generation[i];
        total_in_gen[gen]++;
        if (attended[i]) {
            attended_in_gen[gen]++;
        }
    }

    int max_gen = 0;
    for (int i = 1; i <= N; i++) {
        if (total_in_gen[i] > 0) {
            max_gen = i;
        }
    }

    for (int gen = 1; gen <= max_gen; gen++) {
        double percentage = 0.0;
        if (total_in_gen[gen] > 0) {
            percentage = (100.0 * attended_in_gen[gen]) / total_in_gen[gen];
        }
        cout << fixed << setprecision(2) << percentage;
        if (gen < max_gen) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
