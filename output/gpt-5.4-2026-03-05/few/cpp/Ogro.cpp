#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int E, D;
    if (!(cin >> E >> D)) return 0;

    if (E > D) cout << E + D << '\n';
    else cout << 2 * (D - E) << '\n';

    return 0;
}