
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int none = (N - 2) * (N - 2) * (N - 2);
    int one = 6 * (N - 2) * (N - 2);
    int two = 12 * (N - 2);
    int three = 8;

    if (N == 2) {
        none = 0;
        one = 0;
        two = 0;
        three = 8;
    }

    cout << none << endl;
    cout << one << endl;
    cout << two << endl;
    cout << three << endl;

    return 0;
}
