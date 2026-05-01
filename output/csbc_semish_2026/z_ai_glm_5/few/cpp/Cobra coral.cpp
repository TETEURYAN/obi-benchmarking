
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c, d;
    if (cin >> a >> b >> c >> d) {
        // A falsa coral tem padrão BVPBVP... (período 3).
        // Em qualquer janela de 4 elementos (x_i, x_{i+1}, x_{i+2}, x_{i+3}),
        // como o período é 3, temos x_i = x_{i+3}.
        // Logo, se o primeiro e o último número forem iguais, é uma Falsa Coral (F).
        
        // A coral verdadeira tem padrão BVBPBVBP... (período 4).
        // O ciclo é B, V, B, P. Os elementos B e P são distintos.
        // Em qualquer janela de 4, o primeiro e o último elementos são distintos.
        // (Ex: B,V,B,P -> B!=P; V,B,P,B -> V!=B; B,P,B,V -> B!=V; P,B,V,B -> P!=B).
        // Logo, se o primeiro e o último número forem diferentes, é uma Coral Verdadeira (V).
        
        if (a == d) {
            cout << "F" << endl;
        } else {
            cout << "V" << endl;
        }
    }
    return 0;
}
