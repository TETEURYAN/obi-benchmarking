
#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    vector<int> dist(N, 10000);
    for (int i = 0; i < N; i++) {
        if (A[i] == 0) dist[i] = 0;
    }
    // primeira passagem
    for (int i = 1; i < N; i++) {
        dist[i] = min(dist[i], dist[i - 1] + 1);
    }
    // segunda passagem
    for (int i = N - 2; i >= 0; i--) {
        dist[i] = min(dist[i], dist[i + 1] + 1);
    }
    // output
    for (int i = 0; i < N; i++) {
        if (A[i] == 0) {
            cout << 0;
        } else {
            cout << min(dist[i], 9);
        }
        if (i < N - 1) cout << " ";
        else cout << endl;
    }
    return 0;
}
