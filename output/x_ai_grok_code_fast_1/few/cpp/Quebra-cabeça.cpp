#include <bits/stdc++.h>
using namespace std;

struct Peca {
    int e, d;
    char c;
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    
    vector<Peca> pecas(N);
    vector<int> e_index(200001, -1);
    vector<int> next_piece(N, -1);
    
    for (int i = 0; i < N; i++) {
        int e, d;
        char c;
        cin >> e >> c >> d;
        pecas[i] = {e, d, c};
        e_index[e] = i;
    }
    
    for (int i = 0; i < N; i++) {
        int target = pecas[i].d;
        if (e_index[target] != -1) {
            next_piece[i] = e_index[target];
        }
    }
    
    int current = e_index[0];
    string result = "";
    while (current != -1) {
        result += pecas[current].c;
        current = next_piece[current];
    }
    
    cout << result << endl;
    return 0;
}