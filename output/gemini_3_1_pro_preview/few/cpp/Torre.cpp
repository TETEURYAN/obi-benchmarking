#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> grid(n, vector<int>(n));
    vector<int> row_sum(n, 0);
    vector<int> col_sum(n, 0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> grid[i][j];
            row_sum[i] += grid[i][j];
            col_sum[j] += grid[i][j];
        }
    }

    int max_weight = -1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int weight = row_sum[i] + col_sum[j] - 2 * grid[i][j];
            if (weight > max_weight) {
                max_weight = weight;
            }
        }
    }

    cout << max_weight << "\n";

    return 0;
}