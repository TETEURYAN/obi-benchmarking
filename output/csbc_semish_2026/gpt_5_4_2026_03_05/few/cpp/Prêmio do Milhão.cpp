#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    long long soma = 0;
    for (int i = 1; i <= N; i++) {
        long long A;
        cin >> A;
        soma += A;
        if (soma >= 1000000) {
            cout << i << '\n';
            return 0;
        }
    }

    return 0;
}