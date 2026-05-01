
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int height;
    int index;
    Node *prev, *next;
    Node(int h, int i) : height(h), index(i), prev(nullptr), next(nullptr) {}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<Node*> nodes;
    Node* head = nullptr;
    Node* tail = nullptr;

    for (int i = 0; i < N; ++i) {
        int h;
        cin >> h;
        Node* newNode = new Node(h, i + 1);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        nodes.push_back(newNode);
    }

    int Q;
    cin >> Q;
    int current_size = N;

    while (Q--) {
        int T, I, X;
        cin >> T >> I >> X;
        if (T == 0) {
            Node* newNode = new Node(X, ++current_size);
            if (I == 0) {
                newNode->next = head;
                if (head) head->prev = newNode;
                head = newNode;
                if (!tail) tail = head;
            } else {
                Node* curr = head;
                for (int i = 1; i < I && curr; ++i) {
                    curr = curr->next;
                }
                if (curr) {
                    newNode->next = curr->next;
                    newNode->prev = curr;
                    if (curr->next) {
                        curr->next->prev = newNode;
                    } else {
                        tail = newNode;
                    }
                    curr->next = newNode;
                }
            }
            nodes.push_back(newNode);
        } else {
            Node* curr = head;
            for (int i = 1; i < I && curr; ++i) {
                curr = curr->next;
            }
            if (!curr) {
                cout << "0\n";
                continue;
            }
            int target_height = curr->height + X;
            Node* res = nullptr;
            Node* temp = curr->prev;
            while (temp) {
                if (temp->height > target_height) {
                    res = temp;
                    break;
                }
                temp = temp->prev;
            }
            if (res) {
                cout << res->index << '\n';
            } else {
                cout << "0\n";
            }
        }
    }

    Node* curr = head;
    while (curr) {
        Node* next = curr->next;
        delete curr;
        curr = next;
    }

    return 0;
}
