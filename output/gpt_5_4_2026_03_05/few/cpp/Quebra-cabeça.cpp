#include <bits/stdc++.h>
using namespace std;

struct Piece {
    char c;
    int d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    unordered_map<int, Piece> nxt;
    nxt.reserve((size_t)N * 2);
    nxt.max_load_factor(0.7f);

    for (int i = 0; i < N; i++) {
        int E, D;
        char C;
        cin >> E >> C >> D;
        nxt[E] = {C, D};
    }

    string ans;
    ans.reserve(N);

    int cur = 0;
    for (int i = 0; i < N; i++) {
        auto it = nxt.find(cur);
        ans.push_back(it->second.c);
        cur = it->second.d;
    }

    cout << ans << '\n';
    return 0;
}