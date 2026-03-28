
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (cin >> s) {
        vector<char> tails;
        
        for (char c : s) {
            // Usa upper_bound para encontrar o primeiro elemento maior que c.
            // Isso garante que a subsequência seja não-decrescente (crescente conforme definição do problema).
            auto it = upper_bound(tails.begin(), tails.end(), c);
            
            if (it == tails.end()) {
                tails.push_back(c);
            } else {
                *it = c;
            }
        }
        
        cout << tails.size() << endl;
    }
    return 0;
}
