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

    int maxLen = max(M, N);
    vector<int> res;
    int carry = 0;

    for (int pos = maxLen; pos >= 1; pos--) {
        int idxX = pos - 1;
        int idxY = pos - 1;
        int bitX = (idxX < M) ? X[idxX] : 0;
        int bitY = (idxY < N) ? Y[idxY] : 0;
        int sum = bitX + bitY + carry;
        res.push_back(sum % 2);
        carry = sum / 2;
    }
    if (carry) res.push_back(carry);

    reverse(res.begin(), res.end());

    while (res.size() > 1 && res.back() == 0) res.pop_back();

    for (int i = 0; i < (int)res.size(); i++) {
        if (i) cout << ' ';
        cout << res[i];
    }
    cout << '\n';

    return 0;
}