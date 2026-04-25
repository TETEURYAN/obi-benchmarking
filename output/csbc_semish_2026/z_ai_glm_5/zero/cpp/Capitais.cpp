
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    // Otimização de entrada/saída para competitivo
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    // Grafo representado por lista de adjacência
    vector<vector<int>> adj(N + 1);
    vector<int> degree(N + 1, 0);

    // Leitura das arestas
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    // Fila para a BFS multi-fonte
    queue<int> q;
    // Vetor de distâncias
    vector<int> dist(N + 1, -1);
    // Vetor para rastrear a capital de origem da onda de propagação
    vector<int> source(N + 1, -1);

    // Inicialização: todas as capitais (folhas) são fontes
    for (int i = 1; i <= N; ++i) {
        if (degree[i] == 1) {
            q.push(i);
            dist[i] = 0;
            source[i] = i; // Cada capital é sua própria fonte
        }
    }

    // Execução da BFS
    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            // Se o vizinho ainda não foi visitado, propaga a onda
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                source[v] = source[u];
                q.push(v);
            } else {
                // Se o vizinho já foi visitado, verificamos se as ondas se encontraram
                // Se as fontes são diferentes, encontramos um caminho entre duas capitais distintas
                if (source[v] != source[u]) {
                    // A distância é a soma das distâncias até o ponto de encontro + 1 (aresta que conecta)
                    cout << dist[u] + dist[v] + 1 << endl;
                    return 0;
                }
            }
        }
    }

    return 0;
}
