#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> fita(N);
    for (int i = 0; i < N; i++) {
        cin >> fita[i];
    }

    const int INF = 1e9;
    vector<int> dist(N, INF);

    int lastZero = -INF;
    for (int i = 0; i < N; i++) {
        if (fita[i] == 0) {
            dist[i] = 0;
            lastZero = i;
        } else if (lastZero != -INF) {
            dist[i] = i - lastZero;
        }
    }

    int nextZero = INF;
    for (int i = N - 1; i >= 0; i--) {
        if (fita[i] == 0) {
            nextZero = i;
        } else if (nextZero != INF) {
            dist[i] = min(dist[i], nextZero - i);
        }
    }

    for (int i = 0; i < N; i++) {
        int tom = (dist[i] >= 9) ? 9 : dist[i];
        cout << tom;
        if (i < N - 1) cout << " ";
    }
    cout << endl;

    return 0;
}