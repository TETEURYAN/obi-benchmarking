
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int x1, y1, x2, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;

    bool horizontal = false;
    bool vertical = false;

    if ((x1 <= N/2 && x2 > N/2) || (x2 <= N/2 && x1 > N/2)) {
        horizontal = true;
    }

    if ((y1 <= N/2 && y2 > N/2) || (y2 <= N/2 && y1 > N/2)) {
        vertical = true;
    }

    if (horizontal || vertical) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}
