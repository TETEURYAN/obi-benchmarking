#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X1, Y1, X2, Y2;
    cin >> N;
    cin >> X1 >> Y1;
    cin >> X2 >> Y2;

    bool ok = false;

    if ((X1 <= N / 2 && X2 > N / 2) || (X2 <= N / 2 && X1 > N / 2)) ok = true;
    if ((Y1 <= N / 2 && Y2 > N / 2) || (Y2 <= N / 2 && Y1 > N / 2)) ok = true;

    cout << (ok ? 'S' : 'N') << '\n';
    return 0;
}