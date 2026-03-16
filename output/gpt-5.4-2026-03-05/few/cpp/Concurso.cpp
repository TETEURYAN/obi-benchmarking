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

    int C = (K == 0 ? 101 : a[K - 1]);
    cout << C << '\n';

    return 0;
}