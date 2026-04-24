#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (cin >> n) {
        long long sum = 0;
        int ans = -1;
        for (int i = 1; i <= n; i++) {
            int a;
            cin >> a;
            sum += a;
            if (sum >= 1000000 && ans == -1) {
                ans = i;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}