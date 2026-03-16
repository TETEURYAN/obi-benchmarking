#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;

    long long zero = (N >= 3) ? (N - 2) * (N - 2) * (N - 2) : 0;
    long long one = (N >= 2) ? 6 * (N - 2) * (N - 2) : 0;
    long long two = 12 * (N - 2);
    long long three = 8;

    cout << zero << '\n';
    cout << one << '\n';
    cout << two << '\n';
    cout << three << '\n';

    return 0;
}