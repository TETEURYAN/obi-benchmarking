
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int height;
    int maxHeight;
    int size;
    int priority;
    Node *left, *right;
    Node(int h) : height(h), maxHeight(h), size(1), priority(rand()), left(nullptr), right(nullptr) {}
};

int getSize(Node *node) {
    return node ? node->size : 0;
}

int getMax(Node *node) {
    return node ? node->maxHeight : 0;
}

void update(Node *node) {
    if (!node) return;
    node->size = 1 + getSize(node->left) + getSize(node->right);
    node->maxHeight = max({node->height, getMax(node->left), getMax(node->right)});
}

void split(Node *node, int pos, Node *&left, Node *&right) {
    if (!node) {
        left = right = nullptr;
        return;
    }
    int curPos = getSize(node->left);
    if (curPos < pos) {
        split(node->right, pos - curPos - 1, node->right, right);
        left = node;
    } else {
        split(node->left, pos, left, node->left);
        right = node;
    }
    update(node);
}

Node *merge(Node *left, Node *right) {
    if (!left) return right;
    if (!right) return left;
    if (left->priority > right->priority) {
        left->right = merge(left->right, right);
        update(left);
        return left;
    } else {
        right->left = merge(left, right->left);
        update(right);
        return right;
    }
}

int query(Node *node, int idx, int threshold) {
    if (!node) return 0;
    int leftSize = getSize(node->left);
    if (idx < leftSize) {
        int res = query(node->left, idx, threshold);
        if (res) return res;
        if (node->height > threshold) return leftSize + 1;
        return query(node->right, idx - leftSize - 1, threshold);
    } else if (idx == leftSize) {
        if (node->height > threshold) return leftSize + 1;
        return query(node->right, idx - leftSize - 1, threshold);
    } else {
        return query(node->right, idx - leftSize - 1, threshold);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    srand(time(0));

    int N;
    cin >> N;
    Node *root = nullptr;
    for (int i = 0; i < N; i++) {
        int h;
        cin >> h;
        root = merge(root, new Node(h));
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int T, I;
        long long X;
        cin >> T >> I >> X;
        if (T == 0) {
            Node *left, *right;
            split(root, I, left, right);
            root = merge(merge(left, new Node(X)), right);
        } else {
            Node *left, *mid, *right;
            split(root, I, left, mid);
            split(mid, 1, mid, right);
            int height = mid->height;
            root = merge(merge(left, mid), right);
            int ans = query(root, I, height + X);
            cout << (ans ? ans : 0) << '\n';
        }
    }
    return 0;
}
