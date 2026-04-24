
#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    vector<bool> is_attendee(n + 1, false);
    for (int i = 0; i < m; ++i) {
        int a;
        cin >> a;
        is_attendee[a] = true;
    }

    vector<int> total(n + 1, 0);
    vector<int> attended(n + 1, 0);
    int max_depth = 0;

    queue<pair<int, int>> q;
    q.push({0, 0});

    while (!q.empty()) {
        int u = q.front().first;
        int d = q.front().second;
        q.pop();

        for (int v : adj[u]) {
            int next_d = d + 1;
            total[next_d]++;
            if (is_attendee[v]) {
                attended[next_d]++;
            }
            max_depth = max(max_depth, next_d);
            q.push({v, next_d});
        }
    }

    cout << fixed << setprecision(2);
    for (int d = 1; d <= max_depth; ++d) {
        double percentage = 0.0;
        if (total[d] > 0) {
            percentage = (double)attended[d] * 100.0 / total[d];
        }
        cout << percentage << (d == max_depth ? "" : " ");
    }
    cout << "\n";

    return 0;
}
