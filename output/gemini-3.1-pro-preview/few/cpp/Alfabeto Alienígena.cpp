#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k, n;
    if (!(cin >> k >> n)) return 0;

    string alphabet, message;
    cin >> alphabet >> message;

    bool is_alien[256] = {false};
    for (char c : alphabet) {
        is_alien[(unsigned char)c] = true;
    }

    bool possible = true;
    for (char c : message) {
        if (!is_alien[(unsigned char)c]) {
            possible = false;
            break;
        }
    }

    if (possible) {
        cout << "S\n";
    } else {
        cout << "N\n";
    }

    return 0;
}