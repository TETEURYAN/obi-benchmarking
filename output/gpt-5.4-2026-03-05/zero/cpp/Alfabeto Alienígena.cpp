#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K, N;
    string alfabeto, mensagem;
    
    cin >> K >> N;
    cin >> alfabeto;
    cin >> mensagem;

    unordered_set<char> s(alfabeto.begin(), alfabeto.end());

    for (char c : mensagem) {
        if (!s.count(c)) {
            cout << 'N' << '\n';
            return 0;
        }
    }

    cout << 'S' << '\n';
    return 0;
}