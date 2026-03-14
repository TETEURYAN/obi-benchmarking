#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < N; ++j) {
            grid[i][j] = row[j] - '0';
        }
    }

    vector<vector<int>> nextGrid(N, vector<int>(N));
    for (int step = 0; step < Q; ++step) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int aliveNeighbors = 0;
                for (int di = -1; di <= 1; ++di) {
                    for (int dj = -1; dj <= 1; ++dj) {
                        if (di == 0 && dj == 0) continue;
                        int ni = i + di, nj = j + dj;
                        if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                            aliveNeighbors += grid[ni][nj];
                        }
                    }
                }
                if (grid[i][j] == 1) {
                    nextGrid[i][j] = (aliveNeighbors == 2 || aliveNeighbors == 3) ? 1 : 0;
                } else {
                    nextGrid[i][j] = (aliveNeighbors == 3) ? 1 : 0;
                }
            }
        }
        grid.swap(nextGrid);
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << grid[i][j];
        }
        cout << endl;
    }
    return 0;
}