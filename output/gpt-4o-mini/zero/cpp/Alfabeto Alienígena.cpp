
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int K, N;
    cin >> K >> N;
    unordered_set<char> alienAlphabet;
    string alphabet, message;
    
    cin >> alphabet;
    for (char c : alphabet) {
        alienAlphabet.insert(c);
    }
    
    cin >> message;
    for (char c : message) {
        if (alienAlphabet.find(c) == alienAlphabet.end()) {
            cout << 'N' << endl;
            return 0;
        }
    }
    
    cout << 'S' << endl;
    return 0;
}
