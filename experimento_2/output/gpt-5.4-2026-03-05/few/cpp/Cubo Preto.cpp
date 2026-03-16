#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    if (!(cin >> N)) return 0;

    long long zero = (N - 2) * (N - 2) * (N - 2);
    long long one = 6 * (N - 2) * (N - 2);
    long long two = 12 * (N - 2);
    long long three = 8;

    cout << zero << '\n';
    cout << one << '\n';
    cout << two << '\n';
    cout << three << '\n';

    return 0;
}