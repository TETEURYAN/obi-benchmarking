#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    long long T;
    cin >> N >> K >> T;

    vector<int> P(N + 1), G(N + 1);
    for (int i = 1; i <= N; i++) cin >> P[i];
    vector<int> pos;
    for (int i = 1; i <= N; i++) {
        cin >> G[i];
        if (G[i] == 1) pos.push_back(i);
    }

    const long long INF = (1LL << 60);
    vector<vector<long long>> dp(K + 1, vector<long long>(N + 1, INF));
    vector<vector<int>> val(K + 1, vector<int>(N + 1, -1000000000));

    dp[0][0] = 0;
    val[0][0] = 0;

    for (int i = 1; i <= K; i++) {
        for (int j = i; j <= N - (K - i); j++) {
            long long bestCost = INF;
            int bestVal = -1000000000;
            for (int p = i - 1; p < j; p++) {
                if (dp[i - 1][p] == INF) continue;
                long long c = dp[i - 1][p] + llabs((long long)pos[i - 1] - j);
                int v = val[i - 1][p] + P[j];
                if (c < bestCost || (c == bestCost && v > bestVal)) {
                    bestCost = c;
                    bestVal = v;
                }
            }
            dp[i][j] = bestCost;
            val[i][j] = bestVal;
        }
    }

    int ans = 0;
    for (int j = K; j <= N; j++) {
        if (dp[K][j] <= T) ans = max(ans, val[K][j]);
    }

    cout << ans << '\n';
    return 0;
}