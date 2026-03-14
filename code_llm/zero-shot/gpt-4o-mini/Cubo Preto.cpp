#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int none = (N - 2) * (N - 2) * (N - 2);
    int one = 6 * (N - 2) * (N - 2);
    int two = 12 * (N - 2);
    int three = 8;

    cout << (none < 0 ? 0 : none) << endl;
    cout << (one < 0 ? 0 : one) << endl;
    cout << (two < 0 ? 0 : two) << endl;
    cout << (three < 0 ? 0 : three) << endl;

    return 0;
}