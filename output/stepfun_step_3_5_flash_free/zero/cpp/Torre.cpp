#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    
    vector<vector<int>> matriz(N, vector<int>(N));
    vector<long long> soma_linha(N, 0);
    vector<long long> soma_coluna(N, 0);
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int x;
            cin >> x;
            matriz[i][j] = x;
            soma_linha[i] += x;
            soma_coluna[j] += x;
        }
    }
    
    long long max_peso = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            long long peso = soma_linha[i] + soma_coluna[j] - 2LL * matriz[i][j];
            if (peso > max_peso) max_peso = peso;
        }
    }
    
    cout << max_peso << "\n";
    
    return 0;
}