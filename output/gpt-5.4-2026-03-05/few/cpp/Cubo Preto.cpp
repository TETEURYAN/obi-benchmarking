#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long N;
    if (!(cin >> N)) return 0;

    long long zero = 0, one = 0, two = 0, three = 8;

    if (N >= 3) {
        zero = (N - 2) * (N - 2) * (N - 2);
        one = 6 * (N - 2) * (N - 2);
        two = 12 * (N - 2);
    }

    cout << zero << '\n';
    cout << one << '\n';
    cout << two << '\n';
    cout << three << '\n';

    return 0;
}