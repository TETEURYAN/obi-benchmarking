
#include <iostream>
using namespace std;

int main() {
    int N, x1, y1, x2, y2;
    cin >> N >> x1 >> y1 >> x2 >> y2;
    
    // Verifica se é possível separar as figurinhas com um corte vertical
    bool vertical_possible = (x1 <= N/2 && x2 > N/2) || (x2 <= N/2 && x1 > N/2);
    
    // Verifica se é possível separar as figurinhas com um corte horizontal
    bool horizontal_possible = (y1 <= N/2 && y2 > N/2) || (y2 <= N/2 && y1 > N/2);
    
    if (vertical_possible || horizontal_possible) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }
    
    return 0;
}
