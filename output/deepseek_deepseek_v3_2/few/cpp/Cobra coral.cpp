#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    
    // Padrão verdadeiro: ...BVBPBVBP... -> sequência de 4: a b c b
    // Padrão falso: ...BVPBVP... -> sequência de -4: a b c a
    if (a == c && b == d) {
        cout << "F\n";
    } else if (a == c || b == d) {
        cout << "V\n";
    } else {
        // Caso geral: verdadeiro se (a,b,c,d) é da forma (x,y,z,y)
        // falso se é da forma (x,y,z,x)
        if (b == d) {
            cout << "V\n";
        } else {
            cout << "F\n";
        }
    }
    
    return 0;
}