#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    const int INF = 1e9;
    vector<vector<int>> dist(N, vector<int>(N, INF));
    deque<pair<int, int>> dq;

    dist[0][0] = grid[0][0];
    dq.push_front({0, 0});

    const int dx[4] = {0, 0, 1, -1};
    const int dy[4] = {1, -1, 0, 0};

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        if (x == N-1 && y == N-1) {
            cout << dist[x][y] << '\n';
            return 0;
        }

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int newDist = dist[x][y] + grid[nx][ny];
                if (newDist < dist[nx][ny]) {
                    dist[nx][ny] = newDist;
                    if (grid[nx][ny] == 0) {
                        dq.push_front({nx, ny});
                    } else {
                        dq.push_back({nx, ny});
                    }
                }
            }
        }
    }

    cout << dist[N-1][N-1] << '\n';
    return 0;
}