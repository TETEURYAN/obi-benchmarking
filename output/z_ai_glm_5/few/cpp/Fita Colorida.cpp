#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    const int INF = 1e9;
    vector<int> d(n);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        d[i] = (x == 0) ? 0 : INF;
    }

    // Left to right pass
    for (int i = 1; i < n; i++) {
        d[i] = min(d[i], d[i-1] + 1);
    }

    // Right to left pass
    for (int i = n - 2; i >= 0; i--) {
        d[i] = min(d[i], d[i+1] + 1);
    }

    // Output
    for (int i = 0; i < n; i++) {
        if (d[i] > 9) d[i] = 9;
        cout << d[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}