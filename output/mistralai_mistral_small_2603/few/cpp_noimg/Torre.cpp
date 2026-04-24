#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n));
    vector<long long> row_sum(n, 0), col_sum(n, 0);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
            row_sum[i] += board[i][j];
            col_sum[j] += board[i][j];
        }
    }

    long long max_weight = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            long long weight = row_sum[i] + col_sum[j] - board[i][j];
            if (weight > max_weight) {
                max_weight = weight;
            }
        }
    }

    cout << max_weight << endl;
    return 0;
}