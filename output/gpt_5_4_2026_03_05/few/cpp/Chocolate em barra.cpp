#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, X1, Y1, X2, Y2;
    if (!(cin >> N)) return 0;
    cin >> X1 >> Y1 >> X2 >> Y2;

    bool horizontal = (X1 <= N / 2 && X2 > N / 2) || (X2 <= N / 2 && X1 > N / 2);
    bool vertical = (Y1 <= N / 2 && Y2 > N / 2) || (Y2 <= N / 2 && Y1 > N / 2);

    cout << (horizontal || vertical ? 'S' : 'N') << '\n';
    return 0;
}