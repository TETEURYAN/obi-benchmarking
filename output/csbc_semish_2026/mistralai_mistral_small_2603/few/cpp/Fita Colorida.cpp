#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> fita(n);
    for (int i = 0; i < n; i++) {
        cin >> fita[i];
    }

    vector<int> dist(n, 1e9);
    queue<int> q;

    for (int i = 0; i < n; i++) {
        if (fita[i] == 0) {
            dist[i] = 0;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int pos = q.front();
        q.pop();

        if (pos > 0 && dist[pos-1] > dist[pos] + 1) {
            dist[pos-1] = dist[pos] + 1;
            q.push(pos-1);
        }
        if (pos < n-1 && dist[pos+1] > dist[pos] + 1) {
            dist[pos+1] = dist[pos] + 1;
            q.push(pos+1);
        }
    }

    for (int i = 0; i < n; i++) {
        if (fita[i] == -1) {
            cout << min(dist[i], 9);
        } else {
            cout << fita[i];
        }
        if (i < n-1) cout << ' ';
    }
    cout << '\n';

    return 0;
}