
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int x1, y1, x2, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;

    bool possible = false;

    // Horizontal cut (y coordinate)
    if (y1 <= n/2 && y2 > n/2) possible = true;
    if (y2 <= n/2 && y1 > n/2) possible = true;

    // Vertical cut (x coordinate)
    if (x1 <= n/2 && x2 > n/2) possible = true;
    if (x2 <= n/2 && x1 > n/2) possible = true;

    cout << (possible ? "S" : "N") << endl;

    return 0;
}
