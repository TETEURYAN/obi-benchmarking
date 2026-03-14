#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int K, N;
    cin >> K >> N;

    set<char> alfabeto;
    for (int i = 0; i < K; i++) {
        char c;
        cin >> c;
        alfabeto.insert(c);
    }

    string mensagem;
    cin >> mensagem;

    for (char c : mensagem) {
        if (alfabeto.find(c) == alfabeto.end()) {
            cout << 'N' << endl;
            return 0;
        }
    }

    cout << 'S' << endl;
    return 0;
}