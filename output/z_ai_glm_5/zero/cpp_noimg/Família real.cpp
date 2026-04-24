
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

// Arrays para armazenar pais, gerações e contadores
// O tamanho máximo é 10000, então 10005 é seguro.
vector<int> parent;
vector<int> generation;
vector<int> total_count;
vector<int> attended_count;
vector<bool> is_attendee;

// Função recursiva com memoização para calcular a geração de um descendente
int get_gen(int u) {
    // Se a geração já foi calculada, retorna o valor
    if (generation[u] != -1) {
        return generation[u];
    }
    // Calcula a geração: 1 + geração do pai
    // O pai pode ser o rei (0), cuja geração é 0 (inicializada)
    return generation[u] = get_gen(parent[u]) + 1;
}

int main() {
    // Otimização de I/O para competitivo
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // Redimensionamento dos vetores
    // Índices de 0 a N. 0 é o rei.
    parent.resize(N + 1);
    generation.assign(N + 1, -1);
    is_attendee.assign(N + 1, false);
    
    // O rei (0) está na geração 0
    generation[0] = 0;

    // Leitura dos pais
    for (int i = 1; i <= N; ++i) {
        cin >> parent[i];
    }

    // Leitura dos participantes
    for (int i = 0; i < M; ++i) {
        int id;
        cin >> id;
        is_attendee[id] = true;
    }

    // Vetores para contagem. No pior caso, geração N.
    total_count.assign(N + 2, 0);
    attended_count.assign(N + 2, 0);

    int max_gen = 0;

    // Processa cada descendente
    for (int i = 1; i <= N; ++i) {
        int g = get_gen(i);
        total_count[g]++;
        if (is_attendee[i]) {
            attended_count[g]++;
        }
        if (g > max_gen) {
            max_gen = g;
        }
    }

    // Imprime o resultado
    cout << fixed << setprecision(2);
    for (int i = 1; i <= max_gen; ++i) {
        if (i > 1) {
            cout << " ";
        }
        double percentage = 0.0;
        if (total_count[i] > 0) {
            percentage = (double)attended_count[i] * 100.0 / total_count[i];
        }
        cout << percentage;
    }
    cout << endl;

    return 0;
}
