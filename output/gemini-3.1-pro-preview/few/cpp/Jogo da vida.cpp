#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int step = 0; step < q; step++) {
        vector<string> next_grid = grid;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int alive_neighbors = 0;
                for (int k = 0; k < 8; k++) {
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        if (grid[ni][nj] == '1') {
                            alive_neighbors++;
                        }
                    }
                }

                if (grid[i][j] == '1') {
                    if (alive_neighbors < 2 || alive_neighbors > 3) {
                        next_grid[i][j] = '0';
                    }
                } else {
                    if (alive_neighbors == 3) {
                        next_grid[i][j] = '1';
                    }
                }
            }
        }
        grid = next_grid;
    }

    for (int i = 0; i < n; i++) {
        cout << grid[i] << "\n";
    }

    return 0;
}