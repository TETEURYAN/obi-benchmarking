#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    long long soma = 0;
    for (int i = 1; i <= N; i++) {
        int A;
        cin >> A;
        soma += A;
        if (soma >= 1000000) {
            cout << i << '\n';
            return 0;
        }
    }
    return 0;
}