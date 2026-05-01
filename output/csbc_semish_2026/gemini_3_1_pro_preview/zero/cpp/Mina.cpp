
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> dist(N, vector<int>(N, 1e9));
    deque<pair<int, int>> dq;

    dist[0][0] = 0;
    dq.push_back({0, 0});

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    while (!dq.empty()) {
        auto [r, c] = dq.front();
        dq.pop_front();

        if (r == N - 1 && c == N - 1) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                int weight = grid[nr][nc];
                if (dist[r][c] + weight < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + weight;
                    if (weight == 0) {
                        dq.push_front({nr, nc});
                    } else {
                        dq.push_back({nr, nc});
                    }
                }
            }
        }
    }

    return 0;
}
