#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    long long T;
    if (!(cin >> N >> K >> T)) return 0;

    vector<int> P(N + 1), G(N + 1);
    for (int i = 1; i <= N; i++) cin >> P[i];
    vector<int> pos;
    for (int i = 1; i <= N; i++) {
        cin >> G[i];
        if (G[i] == 1) pos.push_back(i);
    }

    const long long NEG = -(1LL << 60);

    vector<vector<long long>> dp(K + 1, vector<long long>(N + 1, NEG));
    dp[0][0] = 0;

    for (int i = 1; i <= K; i++) {
        int s = pos[i - 1];
        for (int j = i; j <= N - (K - i); j++) {
            long long cost = llabs((long long)s - j);
            long long best = NEG;
            for (int p = i - 1; p < j; p++) {
                if (dp[i - 1][p] == NEG) continue;
                best = max(best, dp[i - 1][p] + P[j] - cost);
            }
            dp[i][j] = best;
        }
    }

    long long ans = 0;
    for (int j = K; j <= N; j++) {
        ans = max(ans, dp[K][j]);
    }

    ans += T;
    if (ans < 0) ans = 0;

    long long sumTop = 0;
    vector<int> all = P;
    sort(all.begin() + 1, all.end(), greater<int>());
    for (int i = 1; i <= K; i++) sumTop += all[i];
    if (ans > sumTop) ans = sumTop;

    cout << ans << '\n';
    return 0;
}