
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (cin >> n) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        
        int half = n / 2;
        
        if ((x1 <= half && x2 > half) || (x1 > half && x2 <= half) ||
            (y1 <= half && y2 > half) || (y1 > half && y2 <= half)) {
            cout << "S\n";
        } else {
            cout << "N\n";
        }
    }
    
    return 0;
}
