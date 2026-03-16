#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int K, N;
    if (!(cin >> K >> N)) return 0;

    string alfabeto, mensagem;
    cin >> alfabeto >> mensagem;

    vector<bool> existe(256, false);
    for (char c : alfabeto) existe[(unsigned char)c] = true;

    for (char c : mensagem) {
        if (!existe[(unsigned char)c]) {
            cout << 'N' << '\n';
            return 0;
        }
    }

    cout << 'S' << '\n';
    return 0;
}