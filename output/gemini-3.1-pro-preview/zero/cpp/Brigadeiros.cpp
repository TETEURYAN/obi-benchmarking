
#pragma GCC optimize("O3")
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    long long T;
    if (!(cin >> N >> K >> T)) return 0;

    vector<int> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
    }

    vector<int> G(N + 1);
    vector<int> orig_count(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        cin >> G[i];
        orig_count[i] = orig_count[i - 1] + G[i];
    }

    int max_possible_swaps = K * (N - K);
    int MAX_C = min((long long)T, (long long)max_possible_swaps);

    vector<vector<vector<int>>> dp(2, vector<vector<int>>(K + 1, vector<int>(MAX_C + 1, -1)));
    vector<vector<pair<int, int>>> modified(2);

    dp[0][0][0] = 0;
    modified[0].push_back({0, 0});

    vector<int> max_c(K + 1, -1);
    max_c[0] = 0;

    for (int i = 1; i <= N; ++i) {
        int curr = i % 2;
        int prev = 1 - curr;

        for (auto& p : modified[curr]) {
            dp[curr][p.first][p.second] = -1;
        }
        modified[curr].clear();

        vector<int> next_max_c(K + 1, -1);
        int min_j = max(0, K - (N - i + 1));
        int max_j = min(i - 1, K);

        for (int j = min_j; j <= max_j; ++j) {
            int limit_c = max_c[j];
            for (int c = 0; c <= limit_c; ++c) {
                if (dp[prev][j][c] != -1) {
                    int c1 = c + abs(j - orig_count[i]);
                    if (c1 <= MAX_C) {
                        if (dp[curr][j][c1] == -1) {
                            modified[curr].push_back({j, c1});
                        }
                        if (dp[curr][j][c1] < dp[prev][j][c]) {
                            dp[curr][j][c1] = dp[prev][j][c];
                        }
                        if (c1 > next_max_c[j]) next_max_c[j] = c1;
                    }

                    if (j + 1 <= K) {
                        int c2 = c + abs(j + 1 - orig_count[i]);
                        if (c2 <= MAX_C) {
                            if (dp[curr][j + 1][c2] == -1) {
                                modified[curr].push_back({j + 1, c2});
                            }
                            if (dp[curr][j + 1][c2] < dp[prev][j][c] + P[i]) {
                                dp[curr][j + 1][c2] = dp[prev][j][c] + P[i];
                            }
                            if (c2 > next_max_c[j + 1]) next_max_c[j + 1] = c2;
                        }
                    }
                }
            }
        }
        max_c = next_max_c;
    }

    int ans = -1;
    for (int c = 0; c <= MAX_C; ++c) {
        ans = max(ans, dp[N % 2][K][c]);
    }

    cout << ans << "\n";

    return 0;
}
