#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    sort(a.begin(), a.end(), greater<int>());

    if (K == 0) {
        cout << 101 << '\n';
    } else {
        cout << a[K - 1] << '\n';
    }

    return 0;
}