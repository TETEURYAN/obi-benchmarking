
#include <iostream>
using namespace std;

int main() {
    int H, M, S, T;
    cin >> H >> M >> S >> T;

    S += T;
    M += S / 60;
    S %= 60;
    H += M / 60;
    M %= 60;
    H %= 24;

    cout << H << endl << M << endl << S << endl;
    return 0;
}
