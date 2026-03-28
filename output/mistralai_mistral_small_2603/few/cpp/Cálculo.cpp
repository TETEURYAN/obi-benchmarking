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

    vector<int> result;
    int carry = 0;
    int i = M - 1, j = N - 1;

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += X[i--];
        if (j >= 0) sum += Y[j--];
        carry = sum / 2;
        result.push_back(sum % 2);
    }

    reverse(result.begin(), result.end());
    for (int k = 0; k < (int)result.size(); k++) {
        cout << result[k] << (k == (int)result.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}