#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

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