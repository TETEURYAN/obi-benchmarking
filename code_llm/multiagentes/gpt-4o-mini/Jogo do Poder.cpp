#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;
const int MAXM = 100000;
int P[MAXN][MAXM], result[MAXN][MAXM];
bool visited[MAXN][MAXM];
int N, M;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void bfs(int startX, int startY) {
    queue<pair<int, long long>> q;
    long long initialPower = P[startX][startY];
    q.push({startX, initialPower});
    visited[startX][startY] = true;
    result[startX][startY] = initialPower;

    while (!q.empty()) {
        auto [x, power] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (!visited[nx][ny] && power >= P[nx][ny]) {
                    visited[nx][ny] = true;
                    long long newPower = power + P[nx][ny];
                    result[nx][ny] = newPower;
                    q.push({nx, newPower});
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> P[i][j];
            result[i][j] = P[i][j];
            visited[i][j] = false;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (!visited[i][j]) {
                bfs(i, j);
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}