#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXM = 1200005;
int bit[MAXM];
int M;

void add(int idx, int val) {
    for (; idx <= M; idx += idx & -idx) bit[idx] += val;
}

int query_bit(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
    return sum;
}

int find_kth(int k) {
    int idx = 0;
    for (int i = 21; i >= 0; i--) {
        int next_idx = idx + (1 << i);
        if (next_idx <= M && bit[next_idx] < k) {
            idx = next_idx;
            k -= bit[idx];
        }
    }
    return idx + 1;
}

int tree_seg[4 * MAXM];

void update(int node, int l, int r, int idx, int val) {
    if (l == r) {
        tree_seg[node] = val;
        return;
    }
    int mid = l + (r - l) / 2;
    if (idx <= mid) update(2 * node, l, mid, idx, val);
    else update(2 * node + 1, mid + 1, r, idx, val);
    tree_seg[node] = max(tree_seg[2 * node], tree_seg[2 * node + 1]);
}

int query_seg(int node, int l, int r, int ql, int qr, long long V) {
    if (l > qr || r < ql || tree_seg[node] <= V) return 0;
    if (l == r) return l;
    int mid = l + (r - l) / 2;
    int res = query_seg(2 * node + 1, mid + 1, r, ql, qr, V);
    if (res != 0) return res;
    return query_seg(2 * node, l, mid, ql, qr, V);
}

struct Op {
    int type, i, x, id;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    int Q;
    cin >> Q;

    vector<Op> ops(Q);
    int k = 0;
    for (int i = 0; i < Q; i++) {
        cin >> ops[i].type >> ops[i].i >> ops[i].x;
        if (ops[i].type == 0) {
            k++;
            ops[i].id = N + k;
        }
    }

    M = N + k;
    if (M == 0) return 0;

    for (int i = 1; i <= M; i++) {
        bit[i] += 1;
        int nxt = i + (i & -i);
        if (nxt <= M) bit[nxt] += bit[i];
    }

    vector<int> final_pos(M + 1);
    for (int i = Q - 1; i >= 0; i--) {
        if (ops[i].type == 0) {
            int p = find_kth(ops[i].i + 1);
            final_pos[ops[i].id] = p;
            add(p, -1);
        }
    }

    for (int i = 1; i <= N; i++) {
        int p = find_kth(1);
        final_pos[i] = p;
        add(p, -1);
    }

    vector<int> H(M + 1);
    for (int i = 1; i <= N; i++) {
        H[final_pos[i]] = A[i];
    }
    for (int i = 0; i < Q; i++) {
        if (ops[i].type == 0) {
            H[final_pos[ops[i].id]] = ops[i].x;
        }
    }

    fill(bit, bit + M + 1, 0);

    for (int i = 1; i <= N; i++) {
        int p = final_pos[i];
        update(1, 1, M, p, H[p]);
        add(p, 1);
    }

    for (int i = 0; i < Q; i++) {
        if (ops[i].type == 0) {
            int p = final_pos[ops[i].id];
            update(1, 1, M, p, H[p]);
            add(p, 1);
        } else {
            int I = ops[i].i;
            long long D = ops[i].x;
            int p = find_kth(I);
            long long height_I = H[p];
            long long target_val = height_I + D;
            int ans_p = 0;
            if (p > 1) {
                ans_p = query_seg(1, 1, M, 1, p - 1, target_val);
            }
            if (ans_p == 0) {
                cout << 0 << "\n";
            } else {
                cout << query_bit(ans_p) << "\n";
            }
        }
    }

    return 0;
}