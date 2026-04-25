#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int a[4];
    for (int i = 0; i < 4; i++) {
        if (!(cin >> a[i])) return 0;
    }
    
    int freq[10] = {0};
    for (int i = 0; i < 4; i++) {
        freq[a[i]]++;
    }
    
    int repeated = -1;
    for (int i = 1; i <= 9; i++) {
        if (freq[i] == 2) {
            repeated = i;
            break;
        }
    }
    
    vector<int> positions;
    for (int i = 0; i < 4; i++) {
        if (a[i] == repeated) {
            positions.push_back(i);
        }
    }
    
    if ((positions[0] == 0 && positions[1] == 3) || (positions[0] == 3 && positions[1] == 0)) {
        cout << 'F' << endl;
    } else {
        cout << 'V' << endl;
    }
    
    return 0;
}