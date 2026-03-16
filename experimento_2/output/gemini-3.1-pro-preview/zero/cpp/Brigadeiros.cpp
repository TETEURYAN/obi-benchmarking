
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int prev_dp[305][2705];
int curr_dp[305][2705];
int P[305];
int s[305];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

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
            s[k_idx++] = i;
        }
    }

    int max_v = 9 * K;
    
    for (int j = 0; j <= N; ++j) {
        for (int v = 0; v <= max_v; ++v) {
            prev_dp[j][v] = INF;
        }
        prev_dp[j][0] = 0;
    }

    for (int i = 1; i <= K; ++i) {
        int limit = 9 * i;
        for (int j = 0; j <= N; ++j) {
            for (int v = 0; v <= limit; ++v) {
                curr_dp[j][v] = INF;
            }
        }
        
        for (int j = i; j <= N; ++j) {
            int p_j = P[j];
            int cost = abs(s[i] - j);
            for (int v = 0; v <= limit; ++v) {
                int res = curr_dp[j - 1][v];
                if (v >= p_j && prev_dp[j - 1][v - p_j] != INF) {
                    int alt = prev_dp[j - 1][v - p_j] + cost;
                    if (alt < res) res = alt;
                }
                curr_dp[j][v] = res;
            }
        }
        
        for (int j = 0; j <= N; ++j) {
            for (int v = 0; v <= limit; ++v) {
                prev_dp[j][v] = curr_dp[j][v];
            }
        }
    }

    int ans = 0;
    for (int v = max_v; v >= 0; --v) {
        if (prev_dp[N][v] != INF && prev_dp[N][v] <= T) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}
