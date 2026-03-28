#include <bits/stdc++.h>
using namespace std;

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

    vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
    dist[0][0] = grid[0][0]; // custo inicial: 0 se livre, 1 se bloqueado (mas início é sempre 0)

    deque<pair<int, int>> dq;
    dq.push_front({0, 0});

    vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        for (auto [dx, dy] : dirs) {
            int nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

            int new_cost = dist[x][y] + grid[nx][ny];
            if (new_cost < dist[nx][ny]) {
                dist[nx][ny] = new_cost;
                if (grid[nx][ny] == -1) { // não ocorre, mas mantém lógica
                    dq.push_back({nx, ny});
                } else if (grid[nx][ny] == 0) {
                    dq.push_front({nx, ny});
                } else { // grid[nx][ny] == 1
                    dq.push_back({nx, ny});
                }
            }
        }
    }

    cout << dist[n-1][n-1] << endl;
    return 0;
}