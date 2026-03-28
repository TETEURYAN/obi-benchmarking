
#include <iostream>

using namespace std;

int main() {
    int N;
    int x1, y1, x2, y2;

    cin >> N >> x1 >> y1 >> x2 >> y2;

    int mid = N / 2;

    // Verifica corte vertical: colunas Y devem estar em lados opostos
    bool vertical = (y1 <= mid && y2 > mid) || (y2 <= mid && y1 > mid);

    // Verifica corte horizontal: linhas X devem estar em lados opostos
    bool horizontal = (x1 <= mid && x2 > mid) || (x2 <= mid && x1 > mid);

    if (vertical || horizontal) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

    return 0;
}
