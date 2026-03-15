
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9;
int min_cost[305][2705];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    long long T;
    if (!(cin >> N >> K >> T)) return 0;

    vector<int> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
    }

    vector<int> A;
    A.push_back(0);
    for (int i = 1; i <= N; ++i) {
        int g;
        cin >> g;
        if (g == 1) {
            A.push_back(i);
        }
    }

    for (int j = 0; j <= K; ++j) {
        for (int v = 0; v <= 9 * K; ++v) {
            min_cost[j][v] = INF;
        }
    }
    min_cost[0][0] = 0;

    for (int i = 1; i <= N; ++i) {
        int p = P[i];
        for (int j = K; j >= 1; --j) {
            int dist = abs(A[j] - i);
            int max_v = 9 * j;
            for (int v = max_v; v >= p; --v) {
                int c = dist + min_cost[j - 1][v - p];
                if (c < min_cost[j][v]) {
                    min_cost[j][v] = c;
                }
            }
        }
    }

    int ans = 0;
    for (int v = 9 * K; v >= 0; --v) {
        if (min_cost[K][v] <= T) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";

    return 0;
}
