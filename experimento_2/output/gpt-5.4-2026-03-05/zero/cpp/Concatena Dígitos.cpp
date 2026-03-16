#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<long long> pref(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
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