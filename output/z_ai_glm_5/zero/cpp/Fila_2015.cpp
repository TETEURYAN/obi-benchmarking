
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

using namespace std;

// Random number generator for priorities
mt19937 rng(1337);

struct Node {
    int val;
    int prio;
    int cnt;
    int max_val;
    Node *l, *r;
    
    Node(int v) : val(v), prio(rng()), cnt(1), max_val(v), l(nullptr), r(nullptr) {}
};

int get_cnt(Node* t) {
    return t ? t->cnt : 0;
}

int get_max(Node* t) {
    return t ? t->max_val : -1; // Heights are >= 1, so -1 is safe for empty
}

void update(Node* t) {
    if (t) {
        t->cnt = 1 + get_cnt(t->l) + get_cnt(t->r);
        t->max_val = max(t->val, max(get_max(t->l), get_max(t->r)));
    }
}

void split(Node* t, int k, Node*& l, Node*& r) {
    if (!t) {
        l = r = nullptr;
        return;
    }
    
    int current_idx = get_cnt(t->l) + 1;
    if (current_idx <= k) {
        split(t->r, k - current_idx, t->r, r);
        l = t;
    } else {
        split(t->l, k, l, t->l);
        r = t;
    }
    update(t);
}

void merge(Node*& t, Node* l, Node* r) {
    if (!l || !r) {
        t = l ? l : r;
    } else if (l->prio > r->prio) {
        merge(l->r, l->r, r);
        t = l;
    } else {
        merge(r->l, l, r->l);
        t = r;
    }
    update(t);
}

// Returns 1-based index of the rightmost element > T, or 0 if not found
int find_last_greater(Node* t, int T) {
    if (!t || t->max_val <= T) return 0;
    
    // Prioritize right subtree for the rightmost element
    int res_r = find_last_greater(t->r, T);
    if (res_r > 0) {
        return get_cnt(t->l) + 1 + res_r;
    }
    
    // Check current node
    if (t->val > T) {
        return get_cnt(t->l) + 1;
    }
    
    // Check left subtree
    return find_last_greater(t->l, T);
}

int get_kth(Node* t, int k) {
    int l_cnt = get_cnt(t->l);
    if (k == l_cnt + 1) return t->val;
    if (k <= l_cnt) return get_kth(t->l, k);
    return get_kth(t->r, k - l_cnt - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    if (!(cin >> N)) return 0;
    
    Node* root = nullptr;
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        merge(root, root, new Node(a));
    }
    
    int Q;
    cin >> Q;
    while (Q--) {
        int T_op, I, X;
        cin >> T_op >> I >> X;
        
        if (T_op == 0) {
            // Insert height X behind I
            // If I=0, insert at beginning (index 1)
            // If I>0, insert at index I+1
            // Split first I elements
            Node *l, *r;
            split(root, I, l, r);
            merge(root, l, new Node(X));
            merge(root, root, r);
        } else {
            // Query I, D=X
            // Find height at I
            int H_i = get_kth(root, I);
            int threshold = H_i + X;
            
            // Search in [1, I-1]
            if (I == 1) {
                cout << 0 << "\n";
            } else {
                Node *l, *r;
                split(root, I - 1, l, r);
                int ans = find_last_greater(l, threshold);
                cout << ans << "\n";
                merge(root, l, r);
            }
        }
    }
    
    return 0;
}
