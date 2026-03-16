#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<long long> pref(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        int d;
        cin >> d;
        pref[i] = pref[i - 1] + d;
    }

    while (Q--) {
        int L, R;
        cin >> L >> R;
        long long len = R - L + 1;
        long long sum = pref[R] - pref[L - 1];
        long long ans = 11LL * (len - 1) * sum;
        cout << ans << '\n';
    }

    return 0;
}