#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9;

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

    vector<int> x;
    x.push_back(0);
    for (int i = 1; i <= N; ++i) {
        int g;
        cin >> g;
        if (g == 1) {
            x.push_back(i);
        }
    }

    T = min(T, (long long)N * N);

    int max_v = 9 * K;
    vector<vector<int>> dp(K + 1, vector<int>(max_v + 1, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= N; ++i) {
        int p = P[i];
        for (int j = K; j >= 1; --j) {
            int cost = abs(x[j] - i);
            int max_v_prev = 9 * (j - 1);
            for (int v_prev = 0; v_prev <= max_v_prev; ++v_prev) {
                if (dp[j - 1][v_prev] != INF) {
                    int new_cost = dp[j - 1][v_prev] + cost;
                    if (new_cost < dp[j][v_prev + p]) {
                        dp[j][v_prev + p] = new_cost;
                    }
                }
            }
        }
    }

    int ans = 0;
    for (int v = max_v; v >= 0; --v) {
        if (dp[K][v] <= T) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}