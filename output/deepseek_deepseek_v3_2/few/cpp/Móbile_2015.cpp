#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, C, D;
    cin >> A >> B >> C >> D;

    if (A == B + C + D && B + C == D && B == C) {
        cout << "S\n";
    } else {
        cout << "N\n";
    }

    return 0;
}