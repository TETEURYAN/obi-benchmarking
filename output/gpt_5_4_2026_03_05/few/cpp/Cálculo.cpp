#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    if (!(cin >> M >> N)) return 0;

    vector<int> X(M), Y(N);
    for (int i = 0; i < M; ++i) cin >> X[i];
    for (int i = 0; i < N; ++i) cin >> Y[i];

    int L = max(M, N);
    vector<int> A(L, 0), B(L, 0);

    for (int i = 0; i < M; ++i) A[L - M + i] = X[i];
    for (int i = 0; i < N; ++i) B[L - N + i] = Y[i];

    vector<int> R(L + 1, 0);
    int carry = 0;

    for (int i = L - 1; i >= 0; --i) {
        int s = A[i] + B[i] + carry;
        R[i + 1] = s & 1;
        carry = s >> 1;
    }
    R[0] = carry;

    if (R[0] == 1) {
        for (int i = 0; i < L; ++i) R[i] = R[i + 1];
        R[L] = 0;
    } else {
        R.erase(R.begin());
    }

    while (!R.empty() && R.back() == 0) R.pop_back();

    for (int i = 0; i < (int)R.size(); ++i) {
        if (i) cout << ' ';
        cout << R[i];
    }
    cout << '\n';

    return 0;
}