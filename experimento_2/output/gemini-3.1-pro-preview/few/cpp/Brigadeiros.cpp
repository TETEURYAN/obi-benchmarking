#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    long long t;
    if (!(cin >> n >> k >> t)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }

    vector<int> pos;
    pos.push_back(0);
    for (int i = 1; i <= n; i++) {
        int g;
        cin >> g;
        if (g == 1) {
            pos.push_back(i);
        }
    }

    int max_v = 9 * k;
    vector<vector<int>> dp(k + 1, vector<int>(max_v + 1, 1e9));
    dp[0][0] = 0;

    for (int j = 1; j <= n; j++) {
        int pj = p[j];
        for (int i = min(j, k); i >= 1; i--) {
            int cost = abs(pos[i] - j);
            int limit = i * 9;
            for (int v = limit; v >= pj; v--) {
                if (dp[i - 1][v - pj] != 1e9) {
                    if (dp[i - 1][v - pj] + cost < dp[i][v]) {
                        dp[i][v] = dp[i - 1][v - pj] + cost;
                    }
                }
            }
        }
    }

    int ans = 0;
    for (int v = max_v; v >= 0; v--) {
        if (dp[k][v] <= t) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}