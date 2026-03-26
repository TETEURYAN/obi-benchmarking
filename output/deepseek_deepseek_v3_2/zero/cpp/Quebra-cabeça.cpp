
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    unordered_map<int, pair<char, int>> pecas;
    unordered_map<int, int> contagemDireita;
    
    for (int i = 0; i < N; i++) {
        int E, D;
        char C;
        cin >> E >> C >> D;
        pecas[E] = {C, D};
        contagemDireita[D]++;
    }
    
    int inicio = -1;
    for (const auto& p : pecas) {
        if (contagemDireita[p.first] == 0) {
            inicio = p.first;
            break;
        }
    }
    
    string resultado;
    int atual = inicio;
    
    while (true) {
        resultado += pecas[atual].first;
        int proximo = pecas[atual].second;
        if (proximo == 1) break;
        atual = proximo;
    }
    
    cout << resultado << '\n';
    
    return 0;
}
