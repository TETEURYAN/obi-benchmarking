
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Otimização de entrada/saída padrão para competitiva
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Matriz para armazenar o tabuleiro
    vector<vector<int>> board(n, vector<int>(n));
    
    // Vetores para armazenar a soma de cada linha e de cada coluna
    vector<int> rowSums(n, 0);
    vector<int> colSums(n, 0);

    // Leitura dos dados e cálculo das somas parciais
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> board[i][j];
            rowSums[i] += board[i][j];
            colSums[j] += board[i][j];
        }
    }

    int maxWeight = -1;

    // Cálculo do peso máximo
    // Peso(i, j) = (SomaLinha[i] - board[i][j]) + (SomaColuna[j] - board[i][j])
    // Peso(i, j) = SomaLinha[i] + SomaColuna[j] - 2 * board[i][j]
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int currentWeight = rowSums[i] + colSums[j] - 2 * board[i][j];
            if (currentWeight > maxWeight) {
                maxWeight = currentWeight;
            }
        }
    }

    cout << maxWeight << endl;

    return 0;
}
