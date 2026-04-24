
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int x1, y1, x2, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    int metade = N / 2;
    bool horizontal = (x1 <= metade && x2 > metade) || (x1 > metade && x2 <= metade);
    bool vertical = (y1 <= metade && y2 > metade) || (y1 > metade && y2 <= metade);
    cout << (horizontal || vertical ? "S" : "N") << endl;
    return 0;
}
