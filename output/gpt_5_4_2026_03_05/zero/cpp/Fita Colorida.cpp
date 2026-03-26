
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> a(N), dist(N, 1000000000);

    for (int i = 0; i < N; i++) cin >> a[i];

    int last = -1000000000;
    for (int i = 0; i < N; i++) {
        if (a[i] == 0) last = i;
        dist[i] = min(dist[i], i - last);
    }

    last = 1000000000;
    for (int i = N - 1; i >= 0; i--) {
        if (a[i] == 0) last = i;
        dist[i] = min(dist[i], last - i);
    }

    for (int i = 0; i < N; i++) {
        cout << min(dist[i], 9);
        if (i + 1 < N) cout << ' ';
    }
    cout << '\n';

    return 0;
}
