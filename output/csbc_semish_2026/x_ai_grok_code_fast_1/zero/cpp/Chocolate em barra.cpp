
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int X1, Y1, X2, Y2;
    cin >> X1 >> Y1;
    cin >> X2 >> Y2;
    int mid = N / 2;
    bool possible = false;
    // Check horizontal cut
    if ((X1 <= mid && X2 > mid) || (X1 > mid && X2 <= mid)) {
        possible = true;
    }
    // Check vertical cut
    if ((Y1 <= mid && Y2 > mid) || (Y1 > mid && Y2 <= mid)) {
        possible = true;
    }
    if (possible) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }
    return 0;
}
