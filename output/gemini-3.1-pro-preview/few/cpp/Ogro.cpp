#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int e, d;
    if (cin >> e >> d) {
        if (e > d) {
            cout << e + d << "\n";
        } else {
            cout << 2 * (d - e) << "\n";
        }
    }
    
    return 0;
}