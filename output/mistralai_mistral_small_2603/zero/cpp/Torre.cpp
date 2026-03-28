
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<vector<int>> board(N, vector<int>(N));
    vector<int> row_sums(N, 0);
    vector<int> col_sums(N, 0);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> board[i][j];
            row_sums[i] += board[i][j];
            col_sums[j] += board[i][j];
        }
    }

    int max_weight = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int weight = row_sums[i] + col_sums[j] - board[i][j];
            if (weight > max_weight) {
                max_weight = weight;
            }
        }
    }

    cout << max_weight << '\n';
    return 0;
}
