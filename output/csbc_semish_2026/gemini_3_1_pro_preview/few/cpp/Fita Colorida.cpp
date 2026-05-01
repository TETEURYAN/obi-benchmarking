#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> dist(n, 1000000);
    int last_zero = -1;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            last_zero = i;
            dist[i] = 0;
        } else if (last_zero != -1) {
            dist[i] = i - last_zero;
        }
    }

    last_zero = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] == 0) {
            last_zero = i;
        } else if (last_zero != -1) {
            dist[i] = min(dist[i], last_zero - i);
        }
    }

    for (int i = 0; i < n; i++) {
        if (dist[i] > 9) {
            dist[i] = 9;
        }
        cout << dist[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}