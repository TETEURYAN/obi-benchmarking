
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int K, N;
    if (!(cin >> K >> N)) return 0;

    string alphabet;
    cin >> alphabet;

    string message;
    cin >> message;

    vector<bool> valid(256, false);
    for (char c : alphabet) {
        valid[(unsigned char)c] = true;
    }

    bool possible = true;
    for (char c : message) {
        if (!valid[(unsigned char)c]) {
            possible = false;
            break;
        }
    }

    if (possible) {
        cout << "S\n";
    } else {
        cout << "N\n";
    }

    return 0;
}
