#include <iostream>
using namespace std;

int main() {
    int E, D;
    cin >> E; 
    cin >> D; 

    int resultado;
    if (E > D) {
        resultado = E + D; 
    } else {
        resultado = 2 * (D - E); 
    }

    cout << resultado << endl; 
    return 0;
}