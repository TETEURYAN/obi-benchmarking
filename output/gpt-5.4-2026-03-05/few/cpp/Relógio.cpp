#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long H, M, S, T;
    if (!(cin >> H >> M >> S >> T)) return 0;

    long long total = H * 3600 + M * 60 + S;
    total = (total + T) % 86400;

    long long nh = total / 3600;
    total %= 3600;
    long long nm = total / 60;
    long long ns = total % 60;

    cout << nh << '\n' << nm << '\n' << ns << '\n';
    return 0;
}