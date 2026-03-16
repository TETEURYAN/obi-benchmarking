#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    int mx = *max_element(a.begin(), a.end());
    int ans = 0;

    for (int h = 0; h < mx; h++) {
        int i = 0;
        while (i < N) {
            if (a[i] <= h) {
                int j = i;
                while (j < N && a[j] <= h) j++;
                ans++;
                i = j;
            } else {
                i++;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}