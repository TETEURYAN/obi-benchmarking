#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> board(n, vector<int>(n));
    vector<long long> row_sums(n, 0);
    vector<long long> col_sums(n, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> board[i][j];
            row_sums[i] += board[i][j];
            col_sums[j] += board[i][j];
        }
    }

    long long max_weight = -1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            long long current_weight = row_sums[i] + col_sums[j] - 2LL * board[i][j];
            if (current_weight > max_weight) {
                max_weight = current_weight;
            }
        }
    }

    cout << max_weight << endl;

    return 0;
}