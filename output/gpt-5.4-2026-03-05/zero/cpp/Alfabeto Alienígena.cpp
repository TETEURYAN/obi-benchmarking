
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K, N;
    string alfabeto, mensagem;
    cin >> K >> N >> alfabeto >> mensagem;

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
