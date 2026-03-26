#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long h;
    int pr, sz;
    long long mx;
    Node *l, *r;
    Node(long long _h, int _pr) : h(_h), pr(_pr), sz(1), mx(_h), l(nullptr), r(nullptr) {}
};

static inline int getsz(Node* t) { return t ? t->sz : 0; }
static inline long long getmx(Node* t) { return t ? t->mx : LLONG_MIN; }

static inline void upd(Node* t) {
    if (!t) return;
    t->sz = 1 + getsz(t->l) + getsz(t->r);
    t->mx = max(t->h, max(getmx(t->l), getmx(t->r)));
}

void split(Node* t, int k, Node*& a, Node*& b) {
    if (!t) {
        a = b = nullptr;
        return;
    }
    if (getsz(t->l) >= k) {
        split(t->l, k, a, t->l);
        b = t;
        upd(b);
    } else {
        split(t->r, k - getsz(t->l) - 1, t->r, b);
        a = t;
        upd(a);
    }
}

Node* merge(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->pr > b->pr) {
        a->r = merge(a->r, b);
        upd(a);
        return a;
    } else {
        b->l = merge(a, b->l);
        upd(b);
        return b;
    }
}

Node* kth(Node* t, int k) {
    while (t) {
        int ls = getsz(t->l);
        if (k == ls + 1) return t;
        if (k <= ls) t = t->l;
        else k -= ls + 1, t = t->r;
    }
    return nullptr;
}

int find_last_greater(Node* t, long long val, int add = 0) {
    if (!t || t->mx <= val) return 0;
    if (getmx(t->r) > val) return find_last_greater(t->r, val, add + getsz(t->l) + 1);
    if (t->h > val) return add + getsz(t->l) + 1;
    return find_last_greater(t->l, val, add);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count());
    Node* root = nullptr;

    for (int i = 0; i < N; ++i) {
        long long a;
        cin >> a;
        root = merge(root, new Node(a, (int)rng()));
    }

    int Q;
    cin >> Q;

    while (Q--) {
        int T, I;
        long long X;
        cin >> T >> I >> X;

        if (T == 0) {
            Node *a, *b;
            split(root, I, a, b);
            root = merge(merge(a, new Node(X, (int)rng())), b);
        } else {
            Node* p = kth(root, I);
            long long target = p->h + X;
            Node *a, *b;
            split(root, I - 1, a, b);
            int ans = find_last_greater(a, target);
            cout << ans << '\n';
            root = merge(a, b);
        }
    }

    return 0;
}