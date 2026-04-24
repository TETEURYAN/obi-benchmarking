#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    long long sum = 0;
    int days = 0;
    const long long TARGET = 1000000LL;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        sum += a;
        days++;
        if (sum >= TARGET) {
            cout << days << endl;
            return 0;
        }
    }

    // O problema garante que a soma chega a 1 milhão, então este ponto nunca é alcançado.
    return 0;
}