#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long d;
        cin >> d;
        pref[i] = pref[i - 1] + d;
    }

    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        long long k = r - l + 1;
        long long s = pref[r] - pref[l - 1];
        long long ans = 11LL * (k - 1) * s;
        cout << ans << "\n";
    }

    return 0;
}