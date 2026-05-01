#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    vector<int> x(m);
    for (int i = 0; i < m; i++) {
        cin >> x[i];
    }

    vector<int> y(n);
    for (int i = 0; i < n; i++) {
        cin >> y[i];
    }

    int len = max(m, n);
    x.resize(len, 0);
    y.resize(len, 0);

    vector<int> res(len);
    int carry = 0;
    for (int i = len - 1; i >= 0; i--) {
        int sum = x[i] + y[i] + carry;
        res[i] = sum % 2;
        carry = sum / 2;
    }

    int last = len - 1;
    while (last >= 0 && res[last] == 0) {
        last--;
    }

    for (int i = 0; i <= last; i++) {
        cout << res[i] << (i == last ? "" : " ");
    }
    cout << "\n";

    return 0;
}