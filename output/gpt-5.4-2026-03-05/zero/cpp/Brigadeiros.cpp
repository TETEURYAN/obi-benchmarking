#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    long long T;
    cin >> N >> K >> T;

    vector<int> P(N + 1), G(N + 1);
    for (int i = 1; i <= N; ++i) cin >> P[i];
    vector<int> pos;
    for (int i = 1; i <= N; ++i) {
        cin >> G[i];
        if (G[i] == 1) pos.push_back(i);
    }

    const long long INF = (1LL << 60);
    vector<vector<long long>> dp(K + 1, vector<long long>(N + 1, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= K; ++i) {
        for (int j = i; j <= N - (K - i); ++j) {
            long long cost = llabs((long long)pos[i - 1] - j);
            long long best = INF;
            for (int p = i - 1; p < j; ++p) {
                if (dp[i - 1][p] == INF) continue;
                best = min(best, dp[i - 1][p] + cost);
            }
            dp[i][j] = best;
        }
    }

    vector<vector<int>> best(K + 1, vector<int>(N + 1, -1e9));
    best[0][0] = 0;

    for (int i = 1; i <= K; ++i) {
        for (int j = i; j <= N - (K - i); ++j) {
            for (int p = i - 1; p < j; ++p) {
                if (best[i - 1][p] < 0) continue;
                long long used = dp[i - 1][p] + llabs((long long)pos[i - 1] - j);
                if (used > T) continue;
                best[i][j] = max(best[i][j], best[i - 1][p] + P[j]);
            }
        }
    }

    int ans = 0;
    for (int j = K; j <= N; ++j) ans = max(ans, best[K][j]);
    cout << ans << '\n';
    return 0;
}