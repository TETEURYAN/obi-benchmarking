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
    for (int h = 1; h <= mx; ++h) {
        bool prev = false;
        for (int i = 0; i < N; ++i) {
            bool cur = (a[i] < h);
            if (cur && !prev) ans++;
            prev = cur;
        }
    }

    cout << ans << '\n';
    return 0;
}