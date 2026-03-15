
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<string> grid(N);
    for (int i = 0; i < N; ++i) {
        cin >> grid[i];
    }

    int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int q = 0; q < Q; ++q) {
        vector<string> next_grid = grid;
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                int alive = 0;
                for (int i = 0; i < 8; ++i) {
                    int nr = r + dx[i];
                    int nc = c + dy[i];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                        if (grid[nr][nc] == '1') {
                            alive++;
                        }
                    }
                }
                if (grid[r][c] == '1') {
                    if (alive < 2 || alive > 3) {
                        next_grid[r][c] = '0';
                    }
                } else {
                    if (alive == 3) {
                        next_grid[r][c] = '1';
                    }
                }
            }
        }
        grid = next_grid;
    }

    for (int i = 0; i < N; ++i) {
        cout << grid[i] << "\n";
    }

    return 0;
}
