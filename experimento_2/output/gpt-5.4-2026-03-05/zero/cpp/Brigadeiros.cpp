#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    long long T;
    cin >> N >> K >> T;

    vector<int> P(N + 1), G(N + 1), pos;
    for (int i = 1; i <= N; i++) cin >> P[i];
    for (int i = 1; i <= N; i++) {
        cin >> G[i];
        if (G[i] == 1) pos.push_back(i);
    }

    const long long INF = (1LL << 60);
    vector<vector<long long>> dp(K + 1, vector<long long>(N + 1, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= K; i++) {
        for (int j = i; j <= N - (K - i); j++) {
            long long cost = llabs((long long)pos[i - 1] - j);
            long long best = INF;
            for (int prev = i - 1; prev < j; prev++) {
                if (dp[i - 1][prev] == INF) continue;
                best = min(best, dp[i - 1][prev] + cost);
            }
            dp[i][j] = best;
        }
    }

    vector<vector<long long>> best(K + 1, vector<long long>(N + 1, -INF));
    for (int j = 1; j <= N; j++) {
        if (dp[1][j] <= T) best[1][j] = P[j];
    }

    for (int i = 2; i <= K; i++) {
        vector<long long> pref(N + 1, -INF);
        for (int j = 1; j <= N; j++) pref[j] = max(pref[j - 1], best[i - 1][j]);
        for (int j = i; j <= N - (K - i); j++) {
            if (dp[i][j] <= T && pref[j - 1] > -INF/2) {
                best[i][j] = pref[j - 1] + P[j];
            }
        }
    }

    long long ans = 0;
    for (int j = K; j <= N; j++) ans = max(ans, best[K][j]);
    cout << ans << '\n';
    return 0;
}