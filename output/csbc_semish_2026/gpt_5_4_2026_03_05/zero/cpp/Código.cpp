#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    int ans = 0;
    for (int i = 0; i + 2 < N; i++) {
        if (a[i] == 1 && a[i + 1] == 0 && a[i + 2] == 0) ans++;
    }

    cout << ans << '\n';
    return 0;
}