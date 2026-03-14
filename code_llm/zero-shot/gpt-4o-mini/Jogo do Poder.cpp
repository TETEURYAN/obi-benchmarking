#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> power(N, vector<int>(M));
    vector<vector<long long>> maxPower(N, vector<long long>(M, 0));

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            cin >> power[i][j];

    vector<int> dirX = {0, 0, 1, -1};
    vector<int> dirY = {1, -1, 0, 0};

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            priority_queue<tuple<long long, int, int>> pq;
            pq.push({power[i][j], i, j});
            vector<vector<bool>> visited(N, vector<bool>(M, false));
            visited[i][j] = true;
            long long currentPower = power[i][j];

            while (!pq.empty()) {
                auto [p, x, y] = pq.top();
                pq.pop();
                currentPower = max(currentPower, p);

                for (int d = 0; d < 4; ++d) {
                    int nx = x + dirX[d], ny = y + dirY[d];
                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && p >= power[nx][ny]) {
                        visited[nx][ny] = true;
                        pq.push({p + power[nx][ny], nx, ny});
                    }
                }
            }
            maxPower[i][j] = currentPower;
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cout << maxPower[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}