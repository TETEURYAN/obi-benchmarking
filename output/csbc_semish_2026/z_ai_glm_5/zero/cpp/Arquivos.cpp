
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Otimização de entrada/saída para passar nos limites de tempo
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long B; // Usamos long long para B para evitar overflow na soma, embora B caiba em int.
    if (!(cin >> N >> B)) return 0;

    vector<long long> files(N);
    for (int i = 0; i < N; ++i) {
        cin >> files[i];
    }

    // Ordenar os tamanhos dos arquivos para aplicar a estratégia gulosa (dois ponteiros)
    sort(files.begin(), files.end());

    int left = 0;
    int right = N - 1;
    int folders = 0;

    // Estratégia Gulosa: Tentar parear o maior arquivo restante com o menor arquivo restante
    while (left <= right) {
        // Se a soma do menor (left) e maior (right) for menor ou igual a B,
        // podemos colocá-los na mesma pasta.
        if (files[left] + files[right] <= B) {
            left++;  // O menor arquivo foi usado
        }
        // O maior arquivo (right) sempre será usado nesta pasta (sozinho ou em par)
        right--; 
        folders++; // Contabiliza a pasta criada
    }

    cout << folders << endl;

    return 0;
}
