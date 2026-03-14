#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K, T;
    cin >> N >> K >> T;
    vector<int> P(N), G(N);
    for (int i = 0; i < N; i++) cin >> P[i];
    for (int i = 0; i < N; i++) cin >> G[i];

    vector<int> positions;
    for (int i = 0; i < N; i++) {
        if (G[i] == 1) positions.push_back(i);
    }

    int maxBrigadeiros = 0;
    for (int i = 0; i < K; i++) {
        int left = max(0, positions[i] - T);
        int right = min(N - 1, positions[i] + T);
        for (int j = left; j <= right; j++) {
            if (G[j] == 0) {
                maxBrigadeiros += P[j];
            }
        }
    }

    cout << maxBrigadeiros << endl;
    return 0;
}