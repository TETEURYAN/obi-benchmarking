
#include <bits/stdc++.h>

using namespace std;

int main() {
    string S;
    cin >> S;
    int N = S.size();
    vector<int> max_len(26, 0);
    int ans = 0;
    for (char ch : S) {
        int c = ch - 'A';
        int max_prev = 0;
        for (int i = 0; i <= c; i++) {
            max_prev = max(max_prev, max_len[i]);
        }
        int curr = 1 + max_prev;
        ans = max(ans, curr);
        max_len[c] = max(max_len[c], curr);
    }
    cout << ans << endl;
    return 0;
}
