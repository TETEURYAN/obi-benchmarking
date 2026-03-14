#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, M, S, T;
    cin >> H >> M >> S >> T;

    int total_seconds = H * 3600 + M * 60 + S;
    int new_total_seconds = total_seconds + T;

    int new_H = (new_total_seconds / 3600) % 24;
    int new_M = (new_total_seconds / 60) % 60;
    int new_S = new_total_seconds % 60;

    cout << new_H << endl;
    cout << new_M << endl;
    cout << new_S << endl;

    return 0;
}