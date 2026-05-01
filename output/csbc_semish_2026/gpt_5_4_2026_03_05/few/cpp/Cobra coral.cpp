#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d;
    if (!(cin >> a >> b >> c >> d)) return 0;

    if (a == c) cout << "V\n";
    else cout << "F\n";

    return 0;
}