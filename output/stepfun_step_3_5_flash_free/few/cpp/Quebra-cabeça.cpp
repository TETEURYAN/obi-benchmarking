#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    const int MAX_VAL = 200000;
    vector<pair<char, int>> left_map(MAX_VAL + 1, {' ', -1});

    for (int i = 0; i < N; i++) {
        int E, D;
        char C;
        cin >> E >> C >> D;
        left_map[E] = {C, D};
    }

    int current = 0;
    string ans;
    ans.reserve(N);

    for (int i = 0; i < N; i++) {
        auto [C, D] = left_map[current];
        ans.push_back(C);
        current = D;
    }

    cout << ans << '\n';
    return 0;
}