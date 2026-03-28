
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Node {
    ll pri, alt, max_alt;
    int size;
    Node *l, *r;
    Node(ll a) : pri(rand()), alt(a), max_alt(a), size(1), l(nullptr), r(nullptr) {}
};

int get_size(Node* t) { return t ? t->size : 0; }

void update(Node* t) {
    if (!t) return;
    t->size = 1 + get_size(t->l) + get_size(t->r);
    t->max_alt = t->alt;
    if (t->l) t->max_alt = max(t->max_alt, t->l->max_alt);
    if (t->r) t->max_alt = max(t->max_alt, t->r->max_alt);
}

void split(Node* t, int k, Node*& a, Node*& b) {
    if (!t) { a = b = nullptr; return; }
    if (get_size(t->l) >= k) {
        split(t->l, k, a, t->l);
        b = t;
    } else {
        split(t->r, k - get_size(t->l) - 1, t->r, b);
        a = t;
    }
    update(t);
}

Node* merge(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->pri > b->pri) {
        a->r = merge(a->r, b);
        update(a);
        return a;
    } else {
        b->l = merge(a, b->l);
        update(b);
        return b;
    }
}

Node* get_kth(Node* t, int k) {
    if (!t) return nullptr;
    if (get_size(t->l) + 1 == k) return t;
    if (get_size(t->l) >= k) return get_kth(t->l, k);
    return get_kth(t->r, k - get_size(t->l) - 1);
}

int find_last_greater(Node* t, ll val, int offset = 0) {
    if (!t) return -1;
    if (t->alt > val) {
        int res = find_last_greater(t->r, val, offset + get_size(t->l) + 1);
        if (res != -1) return res;
        return offset + get_size(t->l);
    } else {
        if (t->r && t->r->max_alt > val) return find_last_greater(t->r, val, offset + get_size(t->l) + 1);
        return -1;
    }
}

int main() {
    srand(time(0));
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    Node* root = nullptr;
    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        Node* novo = new Node(a);
        root = merge(root, novo);
    }
    int Q;
    cin >> Q;
    for (int q = 0; q < Q; ++q) {
        int T, I;
        ll X;
        cin >> T >> I >> X;
        if (T == 0) {
            Node* novo = new Node(X);
            if (I == 0) {
                root = merge(novo, root);
            } else {
                Node *left, *right;
                split(root, I, left, right);
                root = merge(merge(left, novo), right);
            }
        } else {
            Node* person = get_kth(root, I);
            ll H = person->alt;
            ll val = H + X;
            Node *left, *right;
            split(root, I - 1, left, right);
            int rel_pos = find_last_greater(left, val);
            if (rel_pos == -1) {
                cout << 0 << '\n';
            } else {
                cout << rel_pos + 1 << '\n';
            }
            root = merge(left, right);
        }
    }
    return 0;
}
