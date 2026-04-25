#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> a(N);
    int mx = 0;
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    int ans = 0;
    for (int h = 0; h < mx; ++h) {
        int i = 0;
        while (i < N) {
            if (a[i] <= h) {
                ++i;
            } else {
                ++ans;
                while (i < N && a[i] > h) ++i;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}