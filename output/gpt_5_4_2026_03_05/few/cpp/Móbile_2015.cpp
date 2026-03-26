#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int A, B, C, D;
    if (!(cin >> A >> B >> C >> D)) return 0;

    if (A == B + C + D && B + C == D && B == C) cout << "S\n";
    else cout << "N\n";

    return 0;
}