#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int E, D;
    if (cin >> E >> D) {
        cout << ((E > D) ? (E + D) : (2 * (D - E))) << "\n";
    }
    
    return 0;
}