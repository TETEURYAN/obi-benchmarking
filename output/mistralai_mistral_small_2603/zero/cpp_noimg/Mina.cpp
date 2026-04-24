
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

struct Cell {
    int x, y, cost;
};

int main() {
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> dist(N, vector<int>(N, INT_MAX));
    queue<Cell> q;
    q.push({0, 0, grid[0][0]});
    dist[0][0] = grid[0][0];

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    while (!q.empty()) {
        Cell current = q.front();
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int new_cost = current.cost + grid[nx][ny];
                if (new_cost < dist[nx][ny]) {
                    dist[nx][ny] = new_cost;
                    q.push({nx, ny, new_cost});
                }
            }
        }
    }

    cout << dist[N-1][N-1] << endl;
    return 0;
}
