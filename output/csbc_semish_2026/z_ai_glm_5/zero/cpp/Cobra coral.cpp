
#include <iostream>

using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    // Padrão Falsa Coral (tamanho 3): ... B V P B V P ...
    // Janela de 4: B V P B. O primeiro (B) é igual ao quarto (B).
    // Como o padrão repete a cada 3, a posição 4 é igual à posição 1 (4 = 3 + 1).
    // Logo, se a == d, o padrão é o da Falsa Coral (repetição de 3).

    // Padrão Verdadeira (tamanho 4): ... B V B P B V B P ...
    // Janela de 4: B V B P. O primeiro (B) é diferente do quarto (P).
    // Janela deslocada: V B P B. O primeiro (V) é diferente do quarto (B).
    // Logo, se a != d, o padrão é o da Coral Verdadeira (repetição de 4).

    if (a == d) {
        cout << "F" << endl;
    } else {
        cout << "V" << endl;
    }

    return 0;
}
