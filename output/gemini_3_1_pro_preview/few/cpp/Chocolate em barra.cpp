#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (cin >> n) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        int half = n / 2;
        bool possible = false;

        if ((x1 <= half && x2 > half) || (x1 > half && x2 <= half)) {
            possible = true;
        }
        if ((y1 <= half && y2 > half) || (y1 > half && y2 <= half)) {
            possible = true;
        }

        if (possible) {
            cout << "S\n";
        } else {
            cout << "N\n";
        }
    }

    return 0;
}