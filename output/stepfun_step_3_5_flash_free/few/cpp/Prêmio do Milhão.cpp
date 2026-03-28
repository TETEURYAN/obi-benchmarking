#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    long long soma = 0;
    int dias = 0;
    const long long meta = 1000000;

    for (int i = 0; i < N; i++) {
        long long A;
        cin >> A;
        soma += A;
        dias++;
        if (soma >= meta) break;
    }

    cout << dias << endl;
    return 0;
}