#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int e, d;
    if (cin >> e >> d) {
        if (e > d) {
            cout << e + d << "\n";
        } else {
            cout << 2 * (d - e) << "\n";
        }
    }

    return 0;
}