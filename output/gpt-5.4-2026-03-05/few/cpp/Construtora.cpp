#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> a(N);
    int mx = 0;
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    int ans = 0;
    for (int h = 1; h <= mx; h++) {
        for (int i = 0; i < N; ) {
            if (a[i] < h) {
                ans++;
                while (i < N && a[i] < h) i++;
            } else {
                i++;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}