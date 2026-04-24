#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long H, M, S, T;
    cin >> H >> M >> S >> T;

    long long total = H * 3600 + M * 60 + S;
    total = (total + T) % 86400;

    cout << total / 3600 << '\n';
    total %= 3600;
    cout << total / 60 << '\n';
    cout << total % 60 << '\n';

    return 0;
}