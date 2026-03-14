#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<long long> pref(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        long long d;
        cin >> d;
        pref[i] = pref[i - 1] + d;
    }

    for (int i = 0; i < Q; ++i) {
        int L, R;
        cin >> L >> R;
        long long K = R - L + 1;
        long long S = pref[R] - pref[L - 1];
        long long ans = 11LL * S * (K - 1LL);
        cout << ans << "\n";
    }

    return 0;
}