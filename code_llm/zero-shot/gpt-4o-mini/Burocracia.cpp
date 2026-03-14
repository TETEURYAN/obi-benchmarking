#include <iostream>
#include <vector>
using namespace std;

vector<int> p, root;

void restructure(int v) {
    for (int i = 1; i < p.size(); ++i) {
        if (root[i] == v) {
            root[i] = root[v];
            restructure(i);
        }
    }
}

int find_superior(int v, int k) {
    while (k > 0) {
        v = root[v];
        --k;
    }
    return v;
}

int main() {
    int N;
    cin >> N;
    p.resize(N + 1);
    root.resize(N + 1);
    for (int i = 2; i <= N; ++i) {
        cin >> p[i];
        root[i] = p[i];
    }
    root[1] = 1;

    int Q;
    cin >> Q;
    for (int i = 0; i < Q; ++i) {
        int type, v, k;
        cin >> type >> v;
        if (type == 1) {
            cin >> k;
            cout << find_superior(v, k) << endl;
        } else {
            restructure(v);
        }
    }
    return 0;
}