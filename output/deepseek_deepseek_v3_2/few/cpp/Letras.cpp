#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int n = s.size();

    vector<int> dp(26, 0);
    for (char c : s) {
        int idx = c - 'A';
        int best = 0;
        for (int i = 0; i <= idx; i++) {
            best = max(best, dp[i]);
        }
        dp[idx] = max(dp[idx], best + 1);
    }

    int ans = 0;
    for (int i = -0; i < 26; i++) {
        ans = max(ans, dp[i]);
    }
    cout << ans << endl;

    return 0;
}