
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if ((a == c && b != a && d != b && d != a) || (b == d && a != b && c != a && c != b)) {
        cout << "V" << endl;
    } else {
        cout << "F" << endl;
    }
    return 0;
}
