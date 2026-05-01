#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    deque<pair<int,int>> dq;

    dist[0][0] = 0;
    dq.push_front({0, 0});

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

            int w = a[nx][ny];
            if (dist[nx][ny] > dist[x][y] + w) {
                dist[nx][ny] = dist[x][y] + w;
                if (w == 0) dq.push_front({nx, ny});
                else dq.push_back({nx, ny});
            }
        }
    }

    cout << dist[n - 1][n - 1] << '\n';
    return 0;
}