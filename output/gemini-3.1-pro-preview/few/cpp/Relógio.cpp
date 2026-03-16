#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long h, m, s, t;
    if (cin >> h >> m >> s >> t) {
        long long total_seconds = h * 3600 + m * 60 + s + t;
        total_seconds %= 86400;
        
        long long new_h = total_seconds / 3600;
        total_seconds %= 3600;
        long long new_m = total_seconds / 60;
        long long new_s = total_seconds % 60;
        
        cout << new_h << "\n" << new_m << "\n" << new_s << "\n";
    }

    return 0;
}