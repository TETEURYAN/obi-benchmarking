
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<char, int>> next_piece(200005);
    for (int i = 0; i < n; ++i) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        next_piece[e] = {c, d};
    }

    int curr = 0;
    while (true) {
        cout << next_piece[curr].first;
        curr = next_piece[curr].second;
        if (curr == 1) {
            break;
        }
    }
    cout << "\n";

    return 0;
}
