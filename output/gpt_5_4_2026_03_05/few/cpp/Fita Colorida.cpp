#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> a(N), dist(N, (int)1e9);

    for (int i = 0; i < N; i++) {
        cin >> a[i];
        if (a[i] == 0) dist[i] = 0;
    }

    for (int i = 1; i < N; i++) {
        dist[i] = min(dist[i], dist[i - 1] + 1);
    }

    for (int i = N - 2; i >= 0; i--) {
        dist[i] = min(dist[i], dist[i + 1] + 1);
    }

    for (int i = 0; i < N; i++) {
        cout << min(dist[i], 9) << (i + 1 == N ? '\n' : ' ');
    }

    return 0;
}