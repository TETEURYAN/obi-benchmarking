#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long H, M, S, T;
    if (!(cin >> H >> M >> S >> T)) return 0;

    long long total = H * 3600LL + M * 60LL + S;
    total = (total + T) % 86400LL;

    cout << total / 3600LL << '\n';
    total %= 3600LL;
    cout << total / 60LL << '\n';
    cout << total % 60LL << '\n';

    return 0;
}