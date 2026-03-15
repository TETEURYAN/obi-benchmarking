
#include <iostream>
#include <vector>
using namespace std;

vector<int> parent, root;

int find(int x) {
    if (root[x] != x) {
        root[x] = find(root[x]);
    }
    return root[x];
}

void restructure(int v) {
    int new_root = find(v);
    for (int i = 1; i < root.size(); i++) {
        if (find(i) == new_root) {
            root[i] = new_root;
        }
    }
}

int main() {
    int N;
    cin >> N;
    parent.resize(N + 1);
    root.resize(N + 1);
    for (int i = 2; i <= N; i++) {
        cin >> parent[i];
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
            int current = v;
            for (int i = 0; i < k; i++) {
                current = parent[find(current)];
            }
            cout << current << endl;
        } else {
            restructure(v);
        }
    }
    return 0;
}
