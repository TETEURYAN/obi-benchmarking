#include <bits/stdc++.h>
using namespace std;

struct Piece {
    int d;
    char c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    unordered_map<int, Piece> nxt;
    nxt.reserve(N * 2);

    for (int i = 0; i < N; ++i) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        nxt[e] = {d, c};
    }

    string ans;
    ans.reserve(N);

    int cur = 0;
    for (int i = 0; i < N; ++i) {
        auto it = nxt.find(cur);
        ans.push_back(it->second.c);
        cur = it->second.d;
    }

    cout << ans << '\n';
    return 0;
}