
#include <bits/stdc++.h>

using namespace std;

// Define a maximum number of nodes. N + Q can be up to 1.2 * 10^6
const int MAX_NODES = 1200005;

struct Node {
    int val;    // Height of the person
    int prio;   // Random priority for Treap
    int cnt;    // Subtree size
    int max_h;  // Maximum height in the subtree
    int l, r;   // Indices of left and right children
} nodes[MAX_NODES];

int node_cnt = 0;
int root = 0;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

// Creates a new node with the given height
int new_node(int val) {
    ++node_cnt;
    nodes[node_cnt].val = val;
    nodes[node_cnt].prio = rng();
    nodes[node_cnt].cnt = 1;
    nodes[node_cnt].max_h = val;
    nodes[node_cnt].l = 0;
    nodes[node_cnt].r = 0;
    return node_cnt;
}

// Returns the count of a subtree (handles null nodes)
int get_cnt(int t) {
    return t ? nodes[t].cnt : 0;
}

// Returns the max height of a subtree (handles null nodes)
int get_max(int t) {
    return t ? nodes[t].max_h : 0;
}

// Updates node statistics (count and max height)
void update(int t) {
    if (!t) return;
    nodes[t].cnt = 1 + get_cnt(nodes[t].l) + get_cnt(nodes[t].r);
    nodes[t].max_h = max(nodes[t].val, max(get_max(nodes[t].l), get_max(nodes[t].r)));
}

// Splits the tree t into two trees l and r
// l contains the first k elements, r contains the rest
void split(int t, int k, int& l, int& r) {
    if (!t) {
        l = r = 0;
        return;
    }
    int left_size = get_cnt(nodes[t].l);
    if (left_size < k) {
        split(nodes[t].r, k - left_size - 1, nodes[t].r, r);
        l = t;
    } else {
        split(nodes[t].l, k, l, nodes[t].l);
        r = t;
    }
    update(t);
}

// Merges two trees l and r into t
void merge(int& t, int l, int r) {
    if (!l || !r) {
        t = l ? l : r;
    } else if (nodes[l].prio > nodes[r].prio) {
        merge(nodes[l].r, nodes[l].r, r);
        t = l;
    } else {
        merge(nodes[r].l, l, nodes[r].l);
        t = r;
    }
    update(t);
}

// Finds the rightmost position (1-indexed) in the tree t with height > threshold
// Returns 0 if no such person exists
int query(int t, long long threshold) {
    if (!t || nodes[t].max_h <= threshold) return 0;

    // Prioritize searching the right child to find the "closest" (rightmost) person
    int res = query(nodes[t].r, threshold);
    if (res != 0) {
        return get_cnt(nodes[t].l) + 1 + res;
    }

    // Check the current node
    if (nodes[t].val > threshold) {
        return get_cnt(nodes[t].l) + 1;
    }

    // Finally check the left child
    return query(nodes[t].l, threshold);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (cin >> N) {
        for (int i = 0; i < N; ++i) {
            int a;
            cin >> a;
            int node = new_node(a);
            merge(root, root, node);
        }

        int Q;
        cin >> Q;
        while (Q--) {
            int T, I, X;
            cin >> T >> I >> X;

            if (T == 0) {
                // Operation type 0: Insert height X after position I
                int l, r;
                split(root, I, l, r);
                int node = new_node(X);
                merge(root, l, node);
                merge(root, root, r);
            } else {
                // Operation type 1: Query for person at I with parameter D=X
                int l, r, m, r_rest;
                // Split to isolate the prefix [1...I-1]
                split(root, I - 1, l, r);
                // Split to isolate the I-th person
                split(r, 1, m, r_rest);

                int h_p = nodes[m].val;
                long long thresh = (long long)h_p + X;

                // Query the prefix 'l' for the rightmost person taller than thresh
                int ans = query(l, thresh);
                cout << ans << "\n";

                // Merge back to restore the tree
                merge(r, m, r_rest);
                merge(root, l, r);
            }
        }
    }
    return 0;
}
