
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct Node {
    ll value;
    int priority, size;
    Node *left, *right;
    Node(ll v) : value(v), priority(rand()), size(1), left(NULL), right(NULL) {}
};

int get_size(Node* t) { return t ? t->size : 0; }

void update_size(Node* t) {
    if (t) t->size = 1 + get_size(t->left) + get_size(t->right);
}

void split(Node* t, int k, Node*& a, Node*& b) {
    if (!t) { a = b = NULL; return; }
    if (get_size(t->left) >= k) {
        split(t->left, k, a, t->left);
        b = t;
    } else {
        split(t->right, k - get_size(t->left) - 1, t->right, b);
        a = t;
    }
    update_size(t);
}

Node* merge(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->priority > b->priority) {
        a->right = merge(a->right, b);
        update_size(a);
        return a;
    } else {
        b->left = merge(a, b->left);
        update_size(b);
        return b;
    }
}

ll get_kth(Node* t, int k) {
    if (!t) return 0;
    if (get_size(t->left) >= k) return get_kth(t->left, k);
    if (get_size(t->left) + 1 == k) return t->value;
    return get_kth(t->right, k - get_size(t->left) - 1);
}

int find_rightmost_greater(Node* t, ll threshold, int offset) {
    if (!t) return 0;
    int right_res = find_rightmost_greater(t->right, threshold, offset + get_size(t->left) + 1);
    if (right_res) return right_res;
    if (t->value > threshold) return offset + get_size(t->left) + 1;
    int left_res = find_rightmost_greater(t->left, threshold, offset);
    if (left_res) return left_res;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    srand(time(NULL));
    int N;
    cin >> N;
    Node* root = NULL;
    for (int i = 0; i < N; i++) {
        ll a;
        cin >> a;
        Node* newn = new Node(a);
        root = merge(root, newn);
    }
    int Q;
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        int T, I;
        ll X;
        cin >> T >> I >> X;
        if (T == 0) {
            int pos = I + 1;
            Node *L, *R;
            split(root, pos - 1, L, R);
            Node* newn = new Node(X);
            root = merge(merge(L, newn), R);
        } else {
            Node *L, *R;
            split(root, I - 1, L, R);
            ll hi = get_kth(R, 1);
            ll threshold = hi + X;
            int res = find_rightmost_greater(L, threshold, 1);
            cout << res << '\n';
            root = merge(L, R);
        }
    }
    return 0;
}
