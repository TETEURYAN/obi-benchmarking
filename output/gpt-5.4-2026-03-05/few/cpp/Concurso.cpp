#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    sort(A.begin(), A.end(), greater<int>());

    cout << A[K - 1] << '\n';
    return 0;
}