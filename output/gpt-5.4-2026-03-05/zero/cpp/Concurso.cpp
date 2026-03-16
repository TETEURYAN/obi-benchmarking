#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    sort(a.begin(), a.end(), greater<int>());

    if (K == 0) {
        cout << 101 << '\n';
    } else {
        cout << a[K - 1] << '\n';
    }

    return 0;
}