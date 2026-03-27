#include <bits/stdc++.h>
using namespace std;
int main() {
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    const int INF = 1e9;
    vector<vector<int>> dist(N, vector<int>(N, INF));
    dist[0][0] = 0;
    deque<pair<int, int>> dq;
    dq.push_front({0, 0});
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int cost = grid[nx][ny];
                if (dist[nx][ny] > dist[x][y] + cost) {
                    dist[nx][ny] = dist[x][y] + cost;
                    if (cost == 0) dq.push_front({nx, ny});
                    else dq.push_back({nx, ny});
                }
            }
        }
    }
    cout << dist[N - 1][N - 1] << endl;
    return 0;
}