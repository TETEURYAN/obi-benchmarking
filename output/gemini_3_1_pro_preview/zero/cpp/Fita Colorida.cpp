
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> fita(n);
    for (int i = 0; i < n; ++i) {
        cin >> fita[i];
    }

    vector<int> dist(n, 1e9);
    int last_zero = -1;

    for (int i = 0; i < n; ++i) {
        if (fita[i] == 0) {
            dist[i] = 0;
            last_zero = i;
        } else if (last_zero != -1) {
            dist[i] = i - last_zero;
        }
    }

    last_zero = -1;
    for (int i = n - 1; i >= 0; --i) {
        if (fita[i] == 0) {
            dist[i] = 0;
            last_zero = i;
        } else if (last_zero != -1) {
            dist[i] = min(dist[i], last_zero - i);
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << min(9, dist[i]) << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
