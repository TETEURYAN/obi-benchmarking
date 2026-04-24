#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> fita(N);
    for (int i = 0; i < N; i++) {
        cin >> fita[i];
    }

    const int INF = 1e9;
    vector<int> dist(N, INF);

    for (int i = 0; i < N; i++) {
        if (fita[i] == 0) {
            dist[i] = 0;
        }
    }

    for (int i = 1; i < N; i++) {
        if (dist[i-1] != INF) {
            dist[i] = min(dist[i], dist[i-1] + 1);
        }
    }

    for (int i = N-2; i >= 0; i--) {
        if (dist[i+1] != INF) {
            dist[i] = min(dist[i], dist[i+1] + 1);
        }
    }

    for (int i = 0; i < N; i++) {
        if (dist[i] >= 9) {
            dist[i] = 9;
        }
    }

    for (int i = 0; i < N; i++) {
        if (i > 0) cout << " ";
        cout << dist[i];
    }
    cout << endl;

    return 0;
}