EXAMPLES_BY_LANGUAGE = {
    "python": ["""
Exemplo de entrada (Problema: Soma de dois números):
<contexto>
Escreva um programa que leia dois inteiros e imprima a soma.
</contexto>

Resposta esperada:
import sys
a, b = map(int, sys.stdin.read().split())
print(a + b)
""", """
Exemplo de entrada (Problema: Contar células ocupadas):
<contexto>
Dada uma grade de N linhas e M colunas, conte quantos caracteres '1' existem.
</contexto>

Resposta esperada:
import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
grid = input_data[2:]

count = 0
for row in grid:
    count += row.count('1')

print(count)
""", """
Exemplo de entrada (Problema: Grafo/Conectividade):
<contexto>
Dado um grafo com N vértices e M arestas, liste os vizinhos do vértice 1.
</contexto>

Resposta esperada:
import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

print(*(sorted(adj[1])))
"""],
    "cpp": ["""
Exemplo de entrada (Problema: Soma de dois números):
<contexto>
Escreva um programa que leia dois inteiros e imprima a soma.
</contexto>

Resposta esperada:
#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b;
    if (cin >> a >> b) cout << a + b << endl;
    return 0;
}
""", """
Exemplo de entrada (Problema: Contar células ocupadas):
<contexto>
Dada uma grade de N linhas e M colunas, conte quantos caracteres '1' existem.
</contexto>

Resposta esperada:
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int count = 0;
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (char c : row) {
            if (c == '1') count++;
        }
    }

    cout << count << endl;
    return 0;
}
""", """
Exemplo de entrada (Problema: Grafo/Conectividade):
<contexto>
Dado um grafo com N vértices e M arestas, liste os vizinhos do vértice 1 em ordem crescente.
</contexto>

Resposta esperada:
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    sort(adj[1].begin(), adj[1].end());

    for (int i = 0; i < (int)adj[1].size(); i++) {
        cout << adj[1][i] << (i == (int)adj[1].size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
"""]
}
