#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> a(N, vector<int>(N));
    vector<long long> row(N, 0), col(N, 0);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> a[i][j];
            row[i] += a[i][j];
            col[j] += a[i][j];
        }
    }

    long long ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            long long peso = row[i] + col[j] - a[i][j];
            if (peso > ans) ans = peso;
        }
    }

    cout << ans << '\n';
    return 0;
}