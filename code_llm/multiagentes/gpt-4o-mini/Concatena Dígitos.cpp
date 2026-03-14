#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    vector<int> D(N + 1);
    vector<long long> prefix_sum(N + 1, 0);
    vector<long long> potential_sum(N + 1, 0);

    for (int i = 1; i <= N; i++) {
        cin >> D[i];
        prefix_sum[i] = prefix_sum[i - 1] + D[i];
    }

    for (int i = 1; i <= N; i++) {
        long long potential = (N - 1) * D[i] * 10 * (N - 1) + (N - 1) * (prefix_sum[N] - D[i]);
        potential_sum[i] = potential_sum[i - 1] + potential;
    }

    while (Q--) {
        int L, R;
        cin >> L >> R;
        long long result = potential_sum[R] - potential_sum[L - 1];
        cout << result << endl;
    }

    return 0;
}