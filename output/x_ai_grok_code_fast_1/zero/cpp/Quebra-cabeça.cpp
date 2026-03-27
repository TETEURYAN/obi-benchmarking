
#include <bits/stdc++.h>

using namespace std;

struct Piece {
    int E;
    char C;
    int D;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    vector<Piece> pieces(N);
    unordered_map<int, int> piece_by_E;
    for(int i = 0; i < N; i++) {
        cin >> pieces[i].E >> pieces[i].C >> pieces[i].D;
        piece_by_E[pieces[i].E] = i;
    }
    int current = piece_by_E[0];
    string result = "";
    while(true) {
        result += pieces[current].C;
        if(pieces[current].D == 1) break;
        current = piece_by_E[pieces[current].D];
    }
    cout << result << endl;
    return 0;
}
