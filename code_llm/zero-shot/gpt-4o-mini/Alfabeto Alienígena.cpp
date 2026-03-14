#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int K, N;
    cin >> K >> N;
    unordered_set<char> alienAlphabet;
    char c;

    for (int i = 0; i < K; ++i) {
        cin >> c;
        alienAlphabet.insert(c);
    }

    string message;
    cin >> message;

    for (char ch : message) {
        if (alienAlphabet.find(ch) == alienAlphabet.end()) {
            cout << 'N' << endl;
            return 0;
        }
    }

    cout << 'S' << endl;
    return 0;
}