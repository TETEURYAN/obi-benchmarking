
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int step = 0; step < q; ++step) {
        vector<string> next_grid = grid;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int live_neighbors = 0;
                for (int k = 0; k < 8; ++k) {
                    int ni = i + dr[k];
                    int nj = j + dc[k];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        if (grid[ni][nj] == '1') {
                            live_neighbors++;
                        }
                    }
                }
                if (grid[i][j] == '1') {
                    if (live_neighbors < 2 || live_neighbors > 3) {
                        next_grid[i][j] = '0';
                    }
                } else {
                    if (live_neighbors == 3) {
                        next_grid[i][j] = '1';
                    }
                }
            }
        }
        grid = next_grid;
    }

    for (int i = 0; i < n; ++i) {
        cout << grid[i] << "\n";
    }

    return 0;
}
