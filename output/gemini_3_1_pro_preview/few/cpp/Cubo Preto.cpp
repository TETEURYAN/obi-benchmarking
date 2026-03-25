#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long n;
    if (cin >> n) {
        long long zero = (n - 2) * (n - 2) * (n - 2);
        long long one = 6 * (n - 2) * (n - 2);
        long long two = 12 * (n - 2);
        long long three = 8;

        cout << zero << "\n";
        cout << one << "\n";
        cout << two << "\n";
        cout << three << "\n";
    }

    return 0;
}