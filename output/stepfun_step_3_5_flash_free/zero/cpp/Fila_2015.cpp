
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    int prio;
    int size;
    int max_val;
    Node *l, *r;
    Node(int v) : val(v), prio(rand()), size(1), max_val(v), l(NULL), r(NULL) {}
};

int get_size(Node* t) { return t ? t->size : 0; }
int get_max(Node* t) { return t ? t->max_val : INT_MIN; }

void update(Node* t) {
    if (!t) return;
    t->size = 1 + get_size(t->l) + get_size(t->r);
    t->max_val = max(t->val, max(get_max(t->l), get_max(t->r)));
}

void split(Node* t, int k, Node* &a, Node* &b) {
    if (!t) { a = b = NULL; return; }
    int left_size = get_size(t->l);
    if (left_size >= k) {
        split(t->l, k, a, t->l);
        b = t;
        update(b);
    } else {
        split(t->r, k - left_size - 1, t->r, b);
        a = t;
        update(a);
    }
}

Node* merge(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->prio < b->prio) {
        a->r = merge(a->r, b);
        update(a);
        return a;
    } else {
        b->l = merge(a, b->l);
        update(b);
        return b;
    }
}

int find_last_greater(Node* t, int threshold) {
    if (!t || t->max_val <= threshold) return 0;
    if (t->r && t->r->max_val > threshold) {
        return get_size(t->l) + 1 + find_last_greater(t->r, threshold);
    }
    if (t->val > threshold) {
        return get_size(t->l) + 1;
    }
    return find_last_greater(t->l, threshold);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    srand(time(0));

    int N;
    cin >> N;
    Node* root = NULL;
    for (int i = 0; i < N; i++) {
        int h;
        cin >> h;
        root = merge(root, new Node(h));
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int T, I, X;
        cin >> T >> I >> X;
        if (T == 0) {
            Node *left, *right;
            split(root, I, left, right);
            Node* novo = new Node(X);
            root = merge(merge(left, novo), right);
        } else {
            Node *left, *temp;
            split(root, I - 1, left, temp);
            Node *mid, *right;
            split(temp, 1, mid, right);
            int threshold = mid->val + X;
            int ans = find_last_greater(left, threshold);
            cout << ans << '\n';
            temp = merge(mid, right);
            root = merge(left, temp);
        }
    }
    return 0;
}
