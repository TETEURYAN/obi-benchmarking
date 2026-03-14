#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int none = (N > 2) ? (N - 2) * (N - 2) * (N - 2) : 0;
    int one = (N > 2) ? 6 * (N - 2) * (N - 2) : 0;
    int two = (N > 2) ? 12 * (N - 2) : 0;
    int three = 8;

    cout << none << endl;
    cout << one << endl;
    cout << two << endl;
    cout << three << endl;

    return 0;
}