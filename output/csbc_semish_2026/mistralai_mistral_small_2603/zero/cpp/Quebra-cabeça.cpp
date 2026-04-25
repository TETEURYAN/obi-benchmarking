
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    unordered_map<int, pair<char, int>> pieces;
    int start = 0;

    for (int i = 0; i < N; ++i) {
        int E, D;
        char C;
        cin >> E >> C >> D;
        pieces[E] = {C, D};
    }

    string result;
    int current = 0;

    while (pieces.find(current) != pieces.end()) {
        auto [c, next] = pieces[current];
        result += c;
        current = next;
    }

    cout << result << '\n';

    return 0;
}
