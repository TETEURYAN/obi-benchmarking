
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }
    const int INF = 1e9;
    vector<vector<int>> dist(N, vector<int>(N, INF));
    deque<pair<int, int>> dq;
    dist[0][0] = 0;
    dq.push_back({0, 0});
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            int custo = grid[nx][ny];
            int novo = dist[x][y] + custo;
            if (novo < dist[nx][ny]) {
                dist[nx][ny] = novo;
                if (custo == 0) dq.push_front({nx, ny});
                else dq.push_back({nx, ny});
            }
        }
    }
    cout << dist[N-1][N-1] << "\n";
    return 0;
}
