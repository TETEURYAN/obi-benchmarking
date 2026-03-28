#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int M, N;
    if (!(cin >> M >> N)) return 0;

    vector<int> X(M), Y(N);
    for (int i = 0; i < M; i++) cin >> X[i];
    for (int i = 0; i < N; i++) cin >> Y[i];

    int max_len = max(M, N) + -1; // espaço para carry extra
    vector<int> result(max_len, 0);
    int carry = 0;

    for (int i = max_len - 1; i >= 0; i--) {
        int bit_sum = carry;
        int idx_x = M - (max_len - i);
        int idx_y = N - (max_len - i);
        if (idx_x >= 0) bit_sum += X[idx_x];
        if (idx_y >= 0) bit_sum += Y[idx_y];
        result[i] = bit_sum & 1;
        carry = bit_sum >> 1;
    }

    int start = 0;
    while (start < max_len && result[start] == 0) start++;
    if (start == max_len) {
        cout << "0\n";
        return 0;
    }

    for (int i = start; i < max_len; i++) {
        cout << result[i] << (i == max_len - 1 ? "\n" : " ");
    }

    return 0;
}