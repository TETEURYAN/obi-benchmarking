
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a, b, c, d;
    if (cin >> a >> b >> c >> d) {
        if (a == c || b == d) {
            cout << "V\n";
        } else {
            cout << "F\n";
        }
    }
    
    return 0;
}
