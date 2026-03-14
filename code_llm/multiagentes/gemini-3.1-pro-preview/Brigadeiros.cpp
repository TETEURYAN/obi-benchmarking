#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

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

    vector<int> pos_inicial(K + 1);
    int idx = 1;
    for (int i = 1; i <= N; ++i) {
        int g;
        cin >> g;
        if (g == 1) {
            pos_inicial[idx++] = i;
        }
    }

    int max_total_b = K * 9;
    vector<vector<long long>> dp(K + 1, vector<long long>(max_total_b + 1, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= N; ++i) {
        int p_i = P[i];
        for (int j = K; j >= 1; --j) {
            long long dist = abs(i - pos_inicial[j]);
            int max_b = (j - 1) * 9 + p_i;
            
            long long* dp_j = dp[j].data();
            const long long* dp_j_minus_1 = dp[j - 1].data();
            
            for (int b = max_b; b >= p_i; --b) {
                if (dp_j_minus_1[b - p_i] != INF) {
                    long long cost = dp_j_minus_1[b - p_i] + dist;
                    if (cost < dp_j[b]) {
                        dp_j[b] = cost;
                    }
                }
            }
        }
    }

    int ans = 0;
    for (int b = max_total_b; b >= 0; --b) {
        if (dp[K][b] <= T) {
            ans = b;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}