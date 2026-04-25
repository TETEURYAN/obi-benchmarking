#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    vector<int> X(M), Y(N);
    for (int i = 0; i < M; ++i) cin >> X[i];
    for (int i = 0; i < N; ++i) cin >> Y[i];

    int L = max(M, N) + 2;
    vector<int> A(L, 0), B(L, 0), S(L + 1, 0);

    for (int i = 0; i < M; ++i) A[L - M + i] = X[i];
    for (int i = 0; i < N; ++i) B[L - N + i] = Y[i];

    int carry = 0;
    for (int i = L - 1; i >= 0; --i) {
        int sum = A[i] + B[i] + carry;
        S[i + 1] = sum & 1;
        carry = sum >> 1;
    }
    S[0] = carry;

    int start = 0;
    while (start < (int)S.size() - 1 && S[start] == 0) ++start;

    for (int i = start; i < (int)S.size(); ++i) {
        if (i > start) cout << ' ';
        cout << S[i];
    }
    cout << '\n';

    return 0;
}