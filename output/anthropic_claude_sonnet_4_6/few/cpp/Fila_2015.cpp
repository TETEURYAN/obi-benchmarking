Looking at this problem, I need to:

1. Maintain a dynamic sequence (queue) supporting insertions at arbitrary positions
2. For query type 1: given position I, find the nearest person **ahead** (closer to front) of position I whose height > H_I + D

Key observations:
- "ahead" means smaller index (closer to front of queue)
- "nearest" means the largest index that is still < I and has height > H_I + D
- We need to find the closest person in front with height > threshold

This is a complex data structure problem. Let me think about the approach:

- N, Q up to 6×10^5
- We need a dynamic sequence with O(log N) insertions and queries

I'll use an **order-statistic tree** or a **balanced BST** with implicit keys. The key insight for query type 1: find the rightmost position j < i such that height[j] > height[i] + D.

This is essentially: among all elements before position i, find the one with maximum height that is closest to i (but we need the nearest one with height > threshold, not maximum).

Actually: find the largest j < i such that A[j] > A[i] + D.

I'll use a **segment tree on a rope/treap** (implicit treap) that supports:
- Insert at position
- Query: given range [1, i-1], find the rightmost position with value > threshold

The segment tree approach: maintain a segment tree where each node stores the maximum value in its range. For query, search in [1, i-1] for the rightmost element > threshold by traversing the segment tree from right to left.

For dynamic insertions, I'll use a **Fenwick tree with coordinate compression** — but insertions make this hard.

Better: Use an **implicit treap** where each node stores the max value in its subtree. For query: find rightmost in [1, i-1] with value > threshold.

Let me implement an implicit treap with max-subtree info, supporting split/merge and range-max queries with "find rightmost > threshold in prefix".

#include <bits/stdc++.h>
using namespace std;

mt19937 rng(42);

struct Node {
    int val, mx, sz, pri;
    Node *l, *r;
    Node(int v) : val(v), mx(v), sz(1), pri(rng()), l(nullptr), r(nullptr) {}
};

int sz(Node* t) { return t ? t->sz : 0; }
int mx(Node* t) { return t ? t->mx : 0; }

void upd(Node* t) {
    if (t) {
        t->sz = 1 + sz(t->l) + sz(t->r);
        t->mx = max({t->val, mx(t->l), mx(t->r)});
    }
}

pair<Node*,Node*> split(Node* t, int k) {
    if (!t) return {nullptr, nullptr};
    int ls = sz(t->l);
    if (ls >= k) {
        auto [l, r] = split(t->l, k);
        t->l = r; upd(t);
        return {l, t};
    } else {
        auto [l, r] = split(t->r, k - ls - 1);
        t->r = l; upd(t);
        return {t, r};
    }
}

Node* merge(Node* l, Node* r) {
    if (!l) return r;
    if (!r) return l;
    if (l->pri > r->pri) {
        l->r = merge(l->r, r); upd(l); return l;
    } else {
        r->l = merge(l, r->l); upd(r); return r;
    }
}

// Find rightmost position (1-indexed) in subtree with value > threshold
// offset = number of elements before this subtree
int queryRightmost(Node* t, int threshold, int offset) {
    if (!t || t->mx <= threshold) return 0;
    int ls = sz(t->l);
    // Try right subtree first (larger positions)
    int res = queryRightmost(t->r, threshold, offset + ls + 1);
    if (res) return res;
    // Try current node
    if (t->val > threshold) return offset + ls + 1;
    // Try left subtree
    return queryRightmost(t->l, threshold, offset);
}

Node* root = nullptr;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int a; cin >> a;
        root = merge(root, new Node(a));
    }
    int q; cin >> q;
    while (q--) {
        int t, idx; long long x;
        cin >> t >> idx >> x;
        if (t == 0) {
            auto [l, r] = split(root, idx);
            root = merge(merge(l, new Node((int)x)), r);
        } else {
            // Find height of person at position idx
            auto [l, mr] = split(root, idx - 1);
            auto [m, r] = split(mr, 1);
            int hi = m->val;
            root = merge(merge(l, m), r);
            long long threshold = (long long)hi + x;
            if (threshold > 1e9 + 1) { cout << 0 << '\n'; continue; }
            // Find rightmost in [1, idx-1] with val > threshold
            auto [l2, r2] = split(root, idx - 1);
            int ans = queryRightmost(l2, (int)threshold, 0);
            root = merge(l2, r2);
            cout << ans << '\n';
        }
    }
}