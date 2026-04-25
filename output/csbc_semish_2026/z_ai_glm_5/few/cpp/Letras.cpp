
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    if (cin >> s) {
        int pm[26];
        fill(pm, pm + 26, 0);

        for (char c : s) {
            int idx = c - 'A';
            int val = pm[idx] + 1;
            for (int i = idx; i < 26; ++i) {
                if (val > pm[i]) {
                    pm[i] = val;
                } else {
                    break;
                }
            }
        }

        cout << pm[25] << endl;
    }
    return 0;
}
