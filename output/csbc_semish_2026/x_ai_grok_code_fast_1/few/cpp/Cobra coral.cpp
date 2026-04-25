#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    bool verdadeiro = false;
    // B V B P
    if (a == c && b != a && d != a && b != d) verdadeiro = true;
    // V B P B
    if (b == d && a != b && a != d && c != b && c != a) verdadeiro = true;
    // B P B V
    if (a == c && a != b && a != d && b != d && c != b && c != d) verdadeiro = true;
    // P B V B
    if (a != b && a != c && a != d && b == d && c != b && c != d) verdadeiro = true;
    if (verdadeiro) cout << "V" << endl;
    else cout << "F" << endl;
    return 0;
}