#include <bits/stdc++.h>
using namespace std;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> dist(n, vector<int>(n, -1));
    queue<pair<int, int>> q;

    if (grid[0][0] == 1) {
        dist[0][0] = 1;
    } else {
        dist[0][0] = 0;
    }
    q.push({0, 0});

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && dist[nx][ny] == -1) {
                if (grid[nx][ny] == 1) {
                    dist[nx][ny] = dist[x][y] + 1;
                } else {
                    dist[nx][ny] = dist[x][y];
                }
                q.push({nx, ny});
            }
        }
    }

    cout << dist[n-1][n-1] << endl;

    return 0;
}