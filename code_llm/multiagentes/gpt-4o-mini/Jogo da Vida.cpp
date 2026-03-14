#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;

    vector<vector<int>> current(N, vector<int>(N)), next(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < N; j++) {
            current[i][j] = row[j] - '0';
        }
    }

    for (int step = 0; step < Q; step++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int aliveNeighbors = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if (di == 0 && dj == 0) continue;
                        int ni = i + di, nj = j + dj;
                        if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                            aliveNeighbors += current[ni][nj];
                        }
                    }
                }
                if (current[i][j] == 1) {
                    next[i][j] = (aliveNeighbors == 2 || aliveNeighbors == 3) ? 1 : 0;
                } else {
                    next[i][j] = (aliveNeighbors == 3) ? 1 : 0;
                }
            }
        }
        swap(current, next);
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << current[i][j];
        }
        cout << endl;
    }

    return 0;
}