#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int k, n;
    if (!(cin >> k >> n)) return 0;

    string alfabeto;
    cin >> alfabeto;

    string mensagem;
    cin >> mensagem;

    bool alien[256] = {false};
    
    for (char c : alfabeto) {
        alien[(unsigned char)c] = true;
    }

    for (char c : mensagem) {
        if (!alien[(unsigned char)c]) {
            cout << "N\n";
            return 0;
        }
    }

    cout << "S\n";
    return 0;
}