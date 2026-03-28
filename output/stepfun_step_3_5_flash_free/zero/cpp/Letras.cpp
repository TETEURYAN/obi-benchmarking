#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    vector<int> dp(26, 0);
    for (char c : s) {
        int idx = c - 'A';
        int best = 0;
        for (int j = 0; j <= idx; ++j) {
            best = max(best, dp[j]);
        }
        dp[idx] = max(dp[idx], best + 1);
    }
    int ans = 0;
    for (int x : dp) ans = max(ans, x);
    cout << ans << '\n';
    return 0;
}