
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    vector<int> dp(26, 0);
    int max_len = 0;
    for (char c : s) {
        int current = c - 'A';
        int best = 0;
        for (int i = 0; i < current; ++i) {
            best = max(best, dp[i]);
        }
        dp[current] = best + 1;
        max_len = max(max_len, dp[current]);
    }
    cout << max_len << endl;
    return 0;
}
