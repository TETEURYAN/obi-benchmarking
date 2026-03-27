#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    vector<int> dp(26, 0);
    for (char ch : s) {
        int idx = ch - 'A';
        int max_prev = 0;
        for (int i = 0; i <= idx; i++) {
            max_prev = max(max_prev, dp[i]);
        }
        dp[idx] = max(dp[idx], 1 + max_prev);
    }
    int ans = 0;
    for (int x : dp) ans = max(ans, x);
    cout << ans << endl;
    return 0;
}