#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    long long total = 0;
    int days = 0;
    const long long target = 1000000;

    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        total += a;
        days++;
        if (total >= target) {
            break;
        }
    }

    cout << days << endl;

    return 0;
}