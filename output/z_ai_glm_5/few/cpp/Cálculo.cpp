#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    int k = max(m, n);
    // Using 1-based indexing for simplicity: index i corresponds to 2^-i
    vector<int> x(k + 1, 0);
    vector<int> y(k + 1, 0);
    vector<int> z(k + 1, 0);

    for (int i = 1; i <= m; ++i) {
        cin >> x[i];
    }
    for (int i = 1; i <= n; ++i) {
        cin >> y[i];
    }

    int carry = 0;
    for (int i = k; i >= 1; --i) {
        int sum = x[i] + y[i] + carry;
        z[i] = sum % 2;
        carry = sum / 2;
    }

    // Since X + Y < 1, carry must be 0 at the end (no integer part).
    // We just need to format the output correctly.
    
    // Remove trailing zeros to satisfy "menor número de dígitos possível"
    int last = k;
    while (last > 0 && z[last] == 0) {
        last--;
    }

    // Since X, Y > 0, X+Y > 0, so last >= 1 is guaranteed.
    
    for (int i = 1; i <= last; ++i) {
        cout << z[i] << (i == last ? "" : " ");
    }
    cout << "\n";

    return 0;
}