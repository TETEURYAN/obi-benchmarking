
#include <iostream>
#include <vector>
using namespace std;

vector<int> p, root;

int find_root(int x) {
    if (root[x] != x) {
        root[x] = find_root(root[x]);
    }
    return root[x];
}

int main() {
    int N;
    cin >> N;
    p.resize(N + 1);
    root.resize(N + 1);
    
    for (int i = 2; i <= N; ++i) {
        cin >> p[i];
    }
    
    for (int i = 1; i <= N; ++i) {
        root[i] = i;
    }
    
    int Q;
    cin >> Q;
    while (Q--) {
        int type, v, k;
        cin >> type >> v;
        if (type == 1) {
            cin >> k;
            int current = v;
            for (int i = 0; i < k; ++i) {
                current = find_root(p[current]);
            }
            cout << current << endl;
        } else {
            int new_root = find_root(v);
            for (int i = 1; i <= N; ++i) {
                if (find_root(i) == v) {
                    root[i] = new_root;
                }
            }
        }
    }
    return 0;
}
