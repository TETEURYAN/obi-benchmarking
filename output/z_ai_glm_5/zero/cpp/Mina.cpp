
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> grid(N, vector<int>(N));
    // Initialize distance array with a large value (infinity)
    vector<vector<int>> dist(N, vector<int>(N, 1e9));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }

    // 0-1 BFS using a deque
    deque<pair<int, int>> dq;
    
    // Start position (0, 0) has cost 0
    dist[0][0] = 0;
    dq.push_front({0, 0});

    int dr[] = {0, 0, 1, -1};
    int dc[] = {1, -1, 0, 0};

    while (!dq.empty()) {
        pair<int, int> curr = dq.front();
        dq.pop_front();
        int r = curr.first;
        int c = curr.second;

        // If we reached the destination, we can optimize 
        // (though full processing guarantees correctness)
        if (r == N - 1 && c == N - 1) {
            // In 0-1 BFS, the first time we pop a node, it has the minimum distance.
            // However, we continue to let the loop run or break if we just want the value.
            // Breaking here is safe because weights are non-negative.
            // But let's just let the BFS finish or check at the end for simplicity.
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                int weight = grid[nr][nc];
                if (dist[r][c] + weight < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c] + weight;
                    if (weight == 0) {
                        dq.push_front({nr, nc});
                    } else {
                        dq.push_back({nr, nc});
                    }
                }
            }
        }
    }

    cout << dist[N - 1][N - 1] << endl;

    return 0;
}
