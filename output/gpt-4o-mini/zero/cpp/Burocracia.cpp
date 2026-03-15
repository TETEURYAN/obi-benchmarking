
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

void restructure(int v) {
    int new_root = find_root(v);
    for (int i = 1; i < p.size(); i++) {
        if (find_root(i) == v) {
            root[i] = new_root;
        }
    }
}

int main() {
    int N;
    cin >> N;
    p.resize(N + 1);
    root.resize(N + 1);
    for (int i = 2; i <= N; i++) {
        cin >> p[i];
        root[i] = i;
    }
    root[1] = 1;

    int Q;
    cin >> Q;
    while (Q--) {
        int type, v, k;
        cin >> type >> v;
        if (type == 1) {
            cin >> k;
            for (int i = 0; i < k; i++) {
                v = p[find_root(v)];
            }
            cout << v << endl;
        } else {
            restructure(v);
        }
    }
    return 0;
}
