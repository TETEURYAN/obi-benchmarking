#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int half = n / 2;

    bool possible = false;

    // Check horizontal cut (between rows 'half' and 'half + 1')
    // One sticker must be in the top half (row <= half) and the other in the bottom half (row > half)
    if ((x1 <= half && x2 > half) || (x2 <= half && x1 > half)) {
        possible = true;
    }

    // Check vertical cut (between columns 'half' and 'half + 1')
    // One sticker must be in the left half (col <= half) and the other in the right half (col > half)
    if ((y1 <= half && y2 > half) || (y2 <= half && y1 > half)) {
        possible = true;
    }

    if (possible) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}