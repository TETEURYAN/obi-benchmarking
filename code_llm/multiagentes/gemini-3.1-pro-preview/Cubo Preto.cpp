#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (cin >> n) {
        int k = n - 2;
        
        int faces0 = k * k * k;
        int faces1 = 6 * k * k;
        int faces2 = 12 * k;
        int faces3 = 8;
        
        cout << faces0 << "\n";
        cout << faces1 << "\n";
        cout << faces2 << "\n";
        cout << faces3 << "\n";
    }

    return 0;
}