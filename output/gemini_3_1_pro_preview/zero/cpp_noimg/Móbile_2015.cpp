
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b, c, d;
    if (cin >> a >> b >> c >> d) {
        if (a == b + c + d && b + c == d && b == c) {
            cout << "S\n";
        } else {
            cout << "N\n";
        }
    }

    return 0;
}
