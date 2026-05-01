#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    unordered_map<int, pair<char, int>> pieces;
    int start = 0;

    for (int i = 0; i < n; i++) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        pieces[e] = {c, d};
        if (e == 0) start = d;
    }

    string result;
    int current = 0;
    while (current != 1) {
        auto& piece = pieces[current];
        result += piece.first;
        current = piece.second;
    }

    cout << result << endl;
    return 0;
}