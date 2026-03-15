
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> digits(N);
    for (int i = 0; i < N; ++i) {
        cin >> digits[i];
    }

    vector<long long> prefixSum(N + 1, 0);
    vector<long long> prefixPot(N + 1, 0);

    for (int i = 1; i <= N; ++i) {
        prefixSum[i] = prefixSum[i - 1] + digits[i - 1];
        prefixPot[i] = prefixPot[i - 1] + digits[i - 1] * 10 * (i - 1) + digits[i - 1] * prefixSum[i - 1];
    }

    for (int i = 0; i < Q; ++i) {
        int L, R;
        cin >> L >> R;
        long long totalPot = prefixPot[R] - prefixPot[L - 1];
        cout << totalPot << endl;
    }

    return 0;
}
