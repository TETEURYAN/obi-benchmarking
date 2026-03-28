#include <bits/stdc++.h>

using namespace std;

struct Node {
    int l, r;
    int sz;
    int pri;
    int h;
    int max_h;
} tr[1200010];

int root = 0;
int node_cnt = 0;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int new_node(int h) {
    int u = ++node_cnt;
    tr[u].l = tr[u].r = 0;
    tr[u].sz = 1;
    tr[u].pri = rng();
    tr[u].h = tr[u].max_h = h;
    return u;
}

void pushup(int u) {
    if (!u) return;
    tr[u].sz = 1 + tr[tr[u].l].sz + tr[tr[u].r].sz;
    tr[u].max_h = tr[u].h;
    if (tr[u].l) tr[u].max_h = max(tr[u].max_h, tr[tr[u].l].max_h);
    if (tr[u].r) tr[u].max_h = max(tr[u].max_h, tr[tr[u].r].max_h);
}

void split(int u, int k, int &x, int &y) {
    if (!u) {
        x = y = 0;
        return;
    }
    if (tr[tr[u].l].sz + 1 <= k) {
        x = u;
        split(tr[u].r, k - tr[tr[u].l].sz - 1, tr[u].r, y);
        pushup(x);
    } else {
        y = u;
        split(tr[u].l, k, x, tr[u].l);
        pushup(y);
    }
}

int merge(int x, int y) {
    if (!x || !y) return x ? x : y;
    if (tr[x].pri > tr[y].pri) {
        tr[x].r = merge(tr[x].r, y);
        pushup(x);
        return x;
    } else {
        tr[y].l = merge(x, tr[y].l);
        pushup(y);
        return y;
    }
}

int get_h(int u, int k) {
    int lsz = tr[tr[u].l].sz;
    if (k == lsz + 1) return tr[u].h;
    if (k <= lsz) return get_h(tr[u].l, k);
    return get_h(tr[u].r, k - lsz - 1);
}

int find_rightmost(int u, long long target) {
    if (!u) return 0;
    if (tr[u].max_h <= target) return 0;
    if (tr[u].r && tr[tr[u].r].max_h > target) {
        return tr[tr[u].l].sz + 1 + find_rightmost(tr[u].r, target);
    }
    if (tr[u].h > target) {
        return tr[tr[u].l].sz + 1;
    }
    return find_rightmost(tr[u].l, target);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    if (!(cin >> n)) return 0;
    
    for (int i = 1; i <= n; i++) {
        int h;
        cin >> h;
        root = merge(root, new_node(h));
    }
    
    int q;
    if (!(cin >> q)) return 0;
    
    while (q--) {
        int type, i, x;
        cin >> type >> i >> x;
        if (type == 0) {
            int left_tree, right_tree;
            split(root, i, left_tree, right_tree);
            root = merge(merge(left_tree, new_node(x)), right_tree);
        } else {
            long long target = (long long)get_h(root, i) + x;
            int left_tree, right_tree;
            split(root, i - 1, left_tree, right_tree);
            cout << find_rightmost(left_tree, target) << "\n";
            root = merge(left_tree, right_tree);
        }
    }
    
    return 0;
}