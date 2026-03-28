#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> dp(26, 0);
    int max_len = 0;

    for (char c : s) {
        int idx = c - 'A';
        dp[idx] = max(dp[idx], 1);
        for (int i = 0; i < idx; i++) {
            dp[idx] = max(dp[idx], dp[i] + 1);
        }
        max_len = max(max_len, dp[idx]);
    }

    cout << max_len << endl;
    return 0;
}