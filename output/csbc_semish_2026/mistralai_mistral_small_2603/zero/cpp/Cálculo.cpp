
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    vector<int> X(M);
    vector<int> Y(N);

    for (int i = 0; i < M; ++i) {
        cin >> X[i];
    }

    for (int i = 0; i < N; ++i) {
        cin >> Y[i];
    }

    vector<int> sum;
    int carry = 0;
    int i = M - 1, j = N - 1;

    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) total += X[i--];
        if (j >= 0) total += Y[j--];

        carry = total / 2;
        sum.push_back(total % 2);
    }

    reverse(sum.begin(), sum.end());

    for (size_t k = 0; k < sum.size(); ++k) {
        if (k != 0) cout << " ";
        cout << sum[k];
    }
    cout << endl;

    return 0;
}
