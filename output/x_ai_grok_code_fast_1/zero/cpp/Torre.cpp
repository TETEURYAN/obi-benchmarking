
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    vector<long long> row_sum(N, 0);
    vector<long long> col_sum(N, 0);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            row_sum[i] += grid[i][j];
            col_sum[j] += grid[i][j];
        }
    }
    long long max_weight = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            long long weight = row_sum[i] + col_sum[j] - 2LL * grid[i][j];
            if(weight > max_weight) max_weight = weight;
        }
    }
    cout << max_weight << endl;
    return 0;
}
