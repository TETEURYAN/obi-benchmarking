#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector<string> a(N), b(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    int dx[8] = {-1,-1,-1,0,0,1,1,1};
    int dy[8] = {-1,0,1,-1,1,-1,0,1};

    while (Q--) {
        b = a;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int cnt = 0;
                for (int k = 0; k < 8; ++k) {
                    int ni = i + dx[k], nj = j + dy[k];
                    if (ni >= 0 && ni < N && nj >= 0 && nj < N && a[ni][nj] == '1') cnt++;
                }
                if (a[i][j] == '1') {
                    b[i][j] = (cnt == 2 || cnt == 3) ? '1' : '0';
                } else {
                    b[i][j] = (cnt == 3) ? '1' : '0';
                }
            }
        }
        a.swap(b);
    }

    for (int i = 0; i < N; ++i) cout << a[i] << '\n';
    return 0;
}