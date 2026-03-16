#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_val = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] > max_val) {
            max_val = a[i];
        }
    }

    int ans = max_val - a[0];
    for (int i = 1; i < n; i++) {
        if (a[i - 1] > a[i]) {
            ans += a[i - 1] - a[i];
        }
    }

    cout << ans << "\n";

    return 0;
}