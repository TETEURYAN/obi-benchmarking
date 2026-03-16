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
    vector<vector<long long>> dp(K + 1, vector<long long>(N + 1, -INF));
    dp[0][0] = 0;

    for (int i = 1; i <= K; ++i) {
        for (int j = i; j <= N - (K - i); ++j) {
            long long cost = llabs((long long)pos[i - 1] - j);
            long long best = -INF;
            for (int prev = i - 1; prev < j; ++prev) {
                if (dp[i - 1][prev] == -INF) continue;
                best = max(best, dp[i - 1][prev] + P[j] - cost);
            }
            dp[i][j] = best;
        }
    }

    long long ans = 0;
    for (int j = K; j <= N; ++j) {
        if (dp[K][j] == -INF) continue;
        ans = max(ans, dp[K][j]);
    }

    long long base = 0;
    for (int x : pos) base += P[x];

    long long best = 0;
    for (int j = K; j <= N; ++j) {
        if (dp[K][j] == -INF) continue;
        best = max(best, dp[K][j]);
    }

    vector<vector<long long>> pref(K + 1, vector<long long>(N + 1, -INF));
    for (int j = 0; j <= N; ++j) pref[0][j] = 0;

    for (int i = 1; i <= K; ++i) {
        long long mx = -INF;
        for (int j = 1; j <= N; ++j) {
            if (j - 1 >= 0 && dp[i - 1][j - 1] != -INF)
                mx = max(mx, dp[i - 1][j - 1]);
            if (j >= i && j <= N - (K - i) && mx != -INF) {
                long long cost = llabs((long long)pos[i - 1] - j);
                dp[i][j] = max(dp[i][j], mx + P[j] - cost);
            }
        }
    }

    long long answer = 0;
    for (int j = K; j <= N; ++j) {
        if (dp[K][j] == -INF) continue;
        long long gain_minus_cost = dp[K][j];
        answer = max(answer, gain_minus_cost);
    }

    long long finalAns = 0;
    for (int j = K; j <= N; ++j) {
        if (dp[K][j] == -INF) continue;
        long long val = dp[K][j];
        if (val >= -T) finalAns = max(finalAns, val);
    }

    vector<vector<long long>> ndp(K + 1, vector<long long>(N + 1, -INF));
    ndp[0][0] = 0;
    for (int i = 1; i <= K; ++i) {
        long long mx = -INF;
        for (int j = 1; j <= N; ++j) {
            if (ndp[i - 1][j - 1] != -INF)
                mx = max(mx, ndp[i - 1][j - 1]);
            if (j >= i && j <= N - (K - i) && mx != -INF) {
                long long cost = llabs((long long)pos[i - 1] - j);
                ndp[i][j] = mx + P[j] - cost;
            }
        }
    }

    long long ans2 = 0;
    for (int j = K; j <= N; ++j) {
        if (ndp[K][j] != -INF && 0 <= T + ndp[K][j]) {
            ans2 = max(ans2, ndp[K][j]);
        }
    }

    vector<vector<long long>> bestCost(K + 1, vector<long long>(N + 1, INF));
    vector<vector<int>> bestVal(K + 1, vector<int>(N + 1, -1));
    bestCost[0][0] = 0;
    bestVal[0][0] = 0;

    for (int i = 1; i <= K; ++i) {
        for (int j = i; j <= N - (K - i); ++j) {
            for (int prev = i - 1; prev < j; ++prev) {
                if (bestCost[i - 1][prev] == INF) continue;
                long long c = bestCost[i - 1][prev] + llabs((long long)pos[i - 1] - j);
                int v = bestVal[i - 1][prev] + P[j];
                if (v > bestVal[i][j] || (v == bestVal[i][j] && c < bestCost[i][j])) {
                    bestVal[i][j] = v;
                    bestCost[i][j] = c;
                }
            }
        }
    }

    int result = 0;
    for (int j = K; j <= N; ++j) {
        if (bestCost[K][j] <= T) result = max(result, bestVal[K][j]);
    }

    cout << result << '\n';
    return 0;
}