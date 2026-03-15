
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<long long>> power(N, vector<long long>(M));
    vector<vector<long long>> result(N, vector<long long>(M));
    vector<vector<bool>> visited(N, vector<bool>(M, false));
    priority_queue<tuple<long long, int, int>> pq;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> power[i][j];
            result[i][j] = power[i][j];
            pq.emplace(power[i][j], i, j);
        }
    }

    vector<int> dRow = {-1, 1, 0, 0};
    vector<int> dCol = {0, 0, -1, 1};

    while (!pq.empty()) {
        auto [currPower, x, y] = pq.top();
        pq.pop();
        currPower = -currPower;

        if (visited[x][y]) continue;
        visited[x][y] = true;

        for (int k = 0; k < 4; ++k) {
            int newX = x + dRow[k];
            int newY = y + dCol[k];
            if (newX >= 0 && newX < N && newY >= 0 && newY < M) {
                if (currPower >= power[newX][newY]) {
                    long long newPower = currPower + power[newX][newY];
                    if (newPower > result[newX][newY]) {
                        result[newX][newY] = newPower;
                        pq.emplace(-newPower, newX, newY);
                    }
                }
            }
        }
    }

    for (const auto& row : result) {
        for (int j = 0; j < M; ++j) {
            cout << row[j] << (j == M - 1 ? '\n' : ' ');
        }
    }

    return 0;
}
