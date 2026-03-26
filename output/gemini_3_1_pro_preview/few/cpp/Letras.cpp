#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    if (cin >> s) {
        int dp[26] = {0};
        for (char c : s) {
            int val = c - 'A';
            int max_val = 0;
            for (int i = 0; i <= val; i++) {
                if (dp[i] > max_val) {
                    max_val = dp[i];
                }
            }
            dp[val] = max_val + 1;
        }

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (dp[i] > ans) {
                ans = dp[i];
            }
        }
        cout << ans << "\n";
    }

    return 0;
}