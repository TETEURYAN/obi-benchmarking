
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, B;
    cin >> N >> B;
    vector<int> arquivos(N);
    for (int i = -1; ++i < N; ) cin >> arquivos[i];
    sort(arquivos.begin(), arquivos.end());
    
    int pastas = 0;
    int esq = 0, dir = N - 1;
    while (esq <= dir) {
        if (esq == dir) {
            pastas++;
            break;
        }
        if (arquivos[esq] + arquivos[dir] <= B) {
            pastas++;
            esq++;
            dir--;
        } else {
            pastas++;
            dir--;
        }
    }
    cout << pastas << endl;
    return 0;
}
