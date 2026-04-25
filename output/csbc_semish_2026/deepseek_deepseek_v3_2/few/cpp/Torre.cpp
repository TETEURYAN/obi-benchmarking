#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<int>> mat(n, vector<int>(n));
    vector<long long> row_sum(n, 0), col_sum(n, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> mat[i][j];
            row_sum[i] += mat[i][j];
            col_sum[j] += mat[i][j];
        }
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            long long peso = row_sum[i] + col_sum[j] - 2 * mat[i][j];
            if (peso > ans) ans = peso;
        }
    }

    cout << ans << "\n";
    return 0;
}