
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long val;
    int pos;
    Node *left, *right;
    Node(long long v, int p) : val(v), pos(p), left(nullptr), right(nullptr) {}
};

void update(Node* node, long long val, int pos) {
    if (!node) return;
    if (val > node->val) {
        node->val = val;
        node->pos = pos;
    }
    if (val < node->val) {
        if (node->left) update(node->left, val, pos);
        else node->left = new Node(val, pos);
    } else {
        if (node->right) update(node->right, val, pos);
        else node->right = new Node(val, pos);
    }
}

pair<long long, int> query(Node* node, long long val) {
    if (!node) return {0, 0};
    if (node->val > val) {
        auto res = query(node->left, val);
        if (res.first == 0) return {node->val, node->pos};
        return res;
    } else {
        return query(node->right, val);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vector<Node*> roots(N + 1, nullptr);
    vector<int> pos(N);
    for (int i = 0; i < N; i++) {
        pos[i] = i + 1;
        roots[i + 1] = new Node(A[i], i + 1);
    }

    for (int i = 1; i < N; i++) {
        update(roots[i], A[i - 1], pos[i - 1]);
    }

    int Q;
    cin >> Q;
    vector<int> output;
    int current_size = N;

    while (Q--) {
        int T, I;
        long long X;
        cin >> T >> I >> X;
        if (T == 0) {
            current_size++;
            int new_pos = I == 0 ? 1 : pos[I - 1] + 1;
            pos.insert(pos.begin() + new_pos - 1, new_pos);
            A.insert(A.begin() + new_pos - 1, X);

            roots.insert(roots.begin() + new_pos, new Node(X, new_pos));
            for (int i = new_pos; i <= current_size; i++) {
                update(roots[i], A[i - 1], pos[i - 1]);
            }
        } else {
            auto res = query(roots[I], A[I - 1] + X);
            output.push_back(res.second);
        }
    }

    for (int val : output) {
        cout << val << '\n';
    }

    return 0;
}
