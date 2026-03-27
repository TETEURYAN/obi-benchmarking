#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    vector<vector<long long>> mat(N, vector<long long>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> mat[i][j];
        }
    }
    vector<long long> sum_row(N, 0);
    vector<long long> sum_col(N, 0);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            sum_row[i] += mat[i][j];
            sum_col[j] += mat[i][j];
        }
    }
    long long max_weight = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            long long weight = sum_row[i] + sum_col[j] - 2 * mat[i][j];
            if(weight > max_weight) max_weight = weight;
        }
    }
    cout << max_weight << endl;
    return 0;
}