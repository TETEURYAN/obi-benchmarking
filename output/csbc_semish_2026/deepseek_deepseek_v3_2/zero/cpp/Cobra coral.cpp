
#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    
    // Padrão verdadeiro: ...BVBPBVBPBVBP... -> sequência de 4: B V B P
    // Isso significa que a == c e b != d
    // Padrão falso: ...BVPBVPBVPBVP... -> sequência de 4: B V P B
    // Isso significa que a == d e b != c
    
    if (a == c && b != d) {
        cout << "V" << endl;
    } else {
        cout << "F" << endl;
    }
    
    return 0;
}
