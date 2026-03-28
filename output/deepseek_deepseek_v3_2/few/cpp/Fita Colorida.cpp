#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> fita(n);
    queue<int> q;
    vector<int> dist(n, -1);

    for (int i = 0; i < n; i++) {
        cin >> fita[i];
        if (fita[i] == 0) {
            dist[i] = 0;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        int viz[2] = {cur - 1, cur + 1};
        for (int v : viz) {
            if (v >= 0 && v < n && dist[v] == -1) {
                dist[v] = dist[cur] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        int val = min(dist[i], 9);
        cout << val << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}