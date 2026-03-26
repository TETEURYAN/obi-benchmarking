#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    const int MAX = 200001;
    vector<int> proxD(MAX, -1);
    vector<char> letra(MAX, 0);
    for (int i = 0; i < N; i++) {
        int E, D;
        char C;
        cin >> E >> C >> D;
        proxD[E] = D;
        letra[E] = C;
    }
    int atual = 0;
    string resultado;
    while (atual != 1) {
        resultado.push_back(letra[atual]);
        atual = proxD[atual];
    }
    cout << resultado << '\n';
    return 0;
}