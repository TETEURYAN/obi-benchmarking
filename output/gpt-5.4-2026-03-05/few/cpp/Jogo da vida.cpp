#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<string> grid(N), nextGrid(N, string(N, '0'));
    for (int i = 0; i < N; i++) cin >> grid[i];

    int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int step = 0; step < Q; step++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int alive = 0;
                for (int k = 0; k < 8; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    if (ni >= 0 && ni < N && nj >= 0 && nj < N && grid[ni][nj] == '1') {
                        alive++;
                    }
                }

                if (grid[i][j] == '1') {
                    nextGrid[i][j] = (alive == 2 || alive == 3) ? '1' : '0';
                } else {
                    nextGrid[i][j] = (alive == 3) ? '1' : '0';
                }
            }
        }
        grid.swap(nextGrid);
    }

    for (int i = 0; i < N; i++) {
        cout << grid[i] << '\n';
    }

    return 0;
}