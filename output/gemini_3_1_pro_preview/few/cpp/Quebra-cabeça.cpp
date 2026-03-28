#include <bits/stdc++.h>

using namespace std;

int nxt[200005];
char c[200005];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; i++) {
        int e, d;
        char ch;
        cin >> e >> ch >> d;
        nxt[e] = d;
        c[e] = ch;
    }

    int curr = 0;
    for (int i = 0; i < n; i++) {
        cout << c[curr];
        curr = nxt[curr];
    }
    cout << '\n';

    return 0;
}