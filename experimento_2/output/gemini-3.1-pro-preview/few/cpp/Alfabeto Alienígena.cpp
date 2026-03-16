#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k, n;
    if (cin >> k >> n) {
        string alphabet, message;
        cin >> alphabet >> message;

        vector<bool> valid(256, false);
        for (char c : alphabet) {
            valid[(unsigned char)c] = true;
        }

        bool possible = true;
        for (char c : message) {
            if (!valid[(unsigned char)c]) {
                possible = false;
                break;
            }
        }

        if (possible) {
            cout << "S\n";
        } else {
            cout << "N\n";
        }
    }

    return 0;
}