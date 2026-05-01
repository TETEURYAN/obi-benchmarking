
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> seq(4);
    for (int i = 0; i < 4; ++i) {
        cin >> seq[i];
    }

    vector<int> sorted = seq;
    sort(sorted.begin(), sorted.end());

    bool is_coral = false;
    if (sorted[0] == sorted[1] && sorted[2] == sorted[3] && sorted[1] != sorted[2]) {
        if ((seq[0] == seq[2] && seq[1] == seq[3]) || (seq[0] == seq[3] && seq[1] == seq[2])) {
            is_coral = true;
        }
    }

    cout << (is_coral ? "V" : "F") << endl;

    return 0;
}
