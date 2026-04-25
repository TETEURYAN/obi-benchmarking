#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    if (!(cin >> s)) return 0;

    int dp[26] = {};
    for (char c : s) {
        int x = c - 'A';
        int best = 0;
        for (int i = 0; i <= x; i++) {
            best = max(best, dp[i]);
        }
        dp[x] = max(dp[x], best + 1);
    }

    int ans = 0;
    for (int i = 0; i < 26; i++) ans = max(ans, dp[i]);

    cout << ans << '\n';
    return 0;
}