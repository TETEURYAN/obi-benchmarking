
#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    const int INF = 1e9;
    vector<vector<int>> dist(N, vector<int>(N, INF));
    dist[0][0] = 0;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    pq.push({0, 0, 0}); // cost, x, y
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    while(!pq.empty()) {
        auto [cost, x, y] = pq.top(); pq.pop();
        if(cost > dist[x][y]) continue;
        for(int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int newcost = cost + grid[nx][ny];
                if(newcost < dist[nx][ny]) {
                    dist[nx][ny] = newcost;
                    pq.push({newcost, nx, ny});
                }
            }
        }
    }
    cout << dist[N-1][N-1] << endl;
    return 0;
}
