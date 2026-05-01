#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    unordered_map<int, pair<char, int>> pecas;
    unordered_set<int> direitos;

    for (int i = 0; i < n; i++) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        pecas[e] = {c, d};
        direitos.insert(d);
    }

    int atual = 0;
    string resposta;
    resposta.reserve(n);

    while (true) {
        auto& [letra, prox] = pecas[atual];
        resposta.push_back(letra);
        if (prox == 1) break;
        atual = prox;
    }

    cout << resposta << endl;
    return 0;
}