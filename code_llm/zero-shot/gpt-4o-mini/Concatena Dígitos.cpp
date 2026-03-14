#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> D(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> D[i];
    }

    vector<long long> prefixSum(N + 1, 0);
    vector<long long> prefixSumTen(N + 1, 0);
    
    for (int i = 1; i <= N; ++i) {
        prefixSum[i] = prefixSum[i - 1] + D[i];
        prefixSumTen[i] = prefixSumTen[i - 1] + D[i] * 10;
    }

    for (int i = 0; i < Q; ++i) {
        int L, R;
        cin >> L >> R;
        long long total = 0;
        long long sumD = prefixSum[R] - prefixSum[L - 1];
        long long sumTenD = prefixSumTen[R] - prefixSumTen[L - 1];
        total += sumD * (R - L + 1) * 10; // D_i as tens
        total += sumTenD; // D_j as units
        cout << total << endl;
    }

    return 0;
}