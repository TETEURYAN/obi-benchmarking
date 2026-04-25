
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long val;
    int prior;
    Node *esq, *dir;
    int size;
    long long max_val;
    Node(long long v) : val(v), prior(rand()), esq(nullptr), dir(nullptr), size(1), max_val(v) {}
};

int size(Node* t) { return t ? t->size : 0; }

void update(Node* t) {
    if (!t) return;
    t->size = 1 + size(t->esq) + size(t->dir);
    t->max_val = t->val;
    if (t->esq) t->max_val = max(t->max_val, t->esq->max_val);
    if (t->dir) t->max_val = max(t->max_val, t->dir->max_val);
}

void split(Node* t, int k, Node* &l, Node* &r) {
    if (!t) { l = r = nullptr; return; }
    int sz_esq = size(t->esq);
    if (sz_esq >= k) {
        split(t->esq, k, l, t->esq);
        r = t;
        update(r);
    } else {
        split(t->dir, k - sz_esq - 1, t->dir, r);
        l = t;
        update(l);
    }
}

Node* merge(Node* l, Node* r) {
    if (!l || !r) return l ? l : r;
    if (l->prior > r->prior) {
        l->dir = merge(l->dir, r);
        update(l);
        return l;
    } else {
        r->esq = merge(l, r->esq);
        update(r);
        return r;
    }
}

long long get_value(Node* t, int pos) {
    int sz_esq = size(t->esq);
    if (pos <= sz_esq) return get_value(t->esq, pos);
    else if (pos == sz_esq + 1) return t->val;
    else return get_value(t->dir, pos - sz_esq - 1);
}

int find_last_greater(Node* t, long long X, int offset) {
    if (!t || t->max_val <= X) return -1;
    if (t->dir && t->dir->max_val > X) {
        return find_last_greater(t->dir, X, offset + size(t->esq) + 1);
    }
    if (t->val > X) {
        return offset + size(t->esq) + 1;
    }
    return find_last_greater(t->esq, X, offset);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    srand(time(0));

    int N;
    if (!(cin >> N)) return 0;
    Node* raiz = nullptr;
    for (int i = 0; i < N; i++) {
        long long h;
        cin >> h;
        Node* novo = new Node(h);
        Node* left;
        Node* right;
        split(raiz, size(raiz), left, right);
        raiz = merge(merge(left, novo), right);
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int T, I;
        long long X;
        cin >> T >> I >> X;
        if (T == 0) {
            Node* novo = new Node(X);
            Node *left, *right;
            if (I == 0) {
                split(raiz, 0, left, right);
            } else {
                split(raiz, I, left, right);
            }
            raiz = merge(merge(left, novo), right);
        } else {
            long long h = get_value(raiz, I);
            long long threshold = h + X;
            Node *left, *right;
            split(raiz, I - 1, left, right);
            int pos = find_last_greater(left, threshold, 0);
            if (pos == -1) cout << 0 << '\n';
            else cout << pos << '\n';
            raiz = merge(left, right);
        }
    }
    return 0;
}
