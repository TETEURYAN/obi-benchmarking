#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c, d;
    if (cin >> a >> b >> c >> d) {
        if (a == c || b == d) {
            cout << "V\n";
        } else {
            cout << "F\n";
        }
    }

    return 0;
}