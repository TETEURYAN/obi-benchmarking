
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    // Otimização de entrada/saída para competitivo
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Restrições: 0 <= E <= 200000.
    // Usamos um vetor para mapear o número esquerdo (E) para a peça correspondente.
    // O tamanho é 200005 para acomodar o índice máximo com segurança.
    // Cada posição armazena o caractere (C) e o número direito (D).
    vector<pair<char, int>> pieces(200005);

    for (int i = 0; i < n; ++i) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        pieces[e] = {c, d};
    }

    string result = "";
    // O problema afirma que o número esquerdo da primeira peça é sempre 0.
    int current_id = 0;

    // Percorre a cadeia de peças
    while (true) {
        // Recupera a peça atual
        auto p = pieces[current_id];
        
        // Adiciona a letra ao resultado
        result += p.first;
        
        // Se o número direito for 1, chegamos à última peça
        if (p.second == 1) {
            break;
        }
        
        // Atualiza o ID atual para o número direito, que é o número esquerdo da próxima peça
        current_id = p.second;
    }

    cout << result << "\n";

    return 0;
}
