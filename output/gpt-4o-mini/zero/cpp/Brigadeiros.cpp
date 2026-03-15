
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int N, K, T;
    cin >> N >> K >> T;
    vector<int> brigadeiros(N);
    vector<int> grupo;

    for (int i = 0; i < N; i++) {
        cin >> brigadeiros[i];
    }

    for (int i = 0; i < N; i++) {
        int g;
        cin >> g;
        if (g == 1) {
            grupo.push_back(i);
        }
    }

    vector<int> max_brigadeiros;
    for (int pos : grupo) {
        int left = max(0, pos - T);
        int right = min(N - 1, pos + T);
        int max_b = 0;
        for (int j = left; j <= right; j++) {
            max_b = max(max_b, brigadeiros[j]);
        }
        max_brigadeiros.push_back(max_b);
    }

    sort(max_brigadeiros.rbegin(), max_brigadeiros.rend());
    int total = 0;
    for (int i = 0; i < K; i++) {
        total += max_brigadeiros[i];
    }

    cout << total << endl;
    return 0;
}
