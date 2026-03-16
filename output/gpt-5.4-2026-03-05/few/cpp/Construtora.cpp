#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> a(N + 1);
    int mx = 0;
    for (int i = 1; i <= N; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    int ans = 0;
    for (int h = 1; h <= mx; h++) {
        for (int i = 1; i <= N; i++) {
            if (a[i] == h && (i == 1 || a[i - 1] > h)) ans++;
        }
    }

    cout << ans << '\n';
    return 0;
}