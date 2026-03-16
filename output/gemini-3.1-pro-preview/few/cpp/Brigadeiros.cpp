#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9 + 7;
int dp[305][2705];
int P[305];
int x[305];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    long long T;
    if (!(cin >> N >> K >> T)) return 0;

    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
    }

    int k_idx = 1;
    for (int i = 1; i <= N; ++i) {
        int g;
        cin >> g;
        if (g == 1) {
            x[k_idx++] = i;
        }
    }

    for (int j = 0; j <= K; ++j) {
        for (int v = 0; v <= 9 * K; ++v) {
            dp[j][v] = INF;
        }
    }
    dp[0][0] = 0;

    for (int i = 1; i <= N; ++i) {
        int p_i = P[i];
        for (int j = min(i, K); j >= 1; --j) {
            int dist = abs(x[j] - i);
            int max_v_prev = 9 * (j - 1);
            for (int v = max_v_prev; v >= 0; --v) {
                if (dp[j - 1][v] != INF) {
                    int cost = dp[j - 1][v] + dist;
                    if (cost < dp[j][v + p_i]) {
                        dp[j][v + p_i] = cost;
                    }
                }
            }
        }
    }

    int ans = 0;
    for (int v = 9 * K; v >= 0; --v) {
        if (dp[K][v] != INF && dp[K][v] <= T) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}