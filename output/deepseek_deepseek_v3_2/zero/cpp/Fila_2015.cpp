
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int height;
    int idx;
    Node *prev, *next;
    Node(int h, int i) : height(h), idx(i), prev(nullptr), next(nullptr) {}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    vector<Node*> nodes(N + 1);
    Node *head = nullptr, *tail = nullptr;
    
    for (int i = 1; i <= N; i++) {
        int h;
        cin >> h;
        Node *node = new Node(h, i);
        nodes[i] = node;
        
        if (!head) {
            head = tail = node;
        } else {
            tail->next = node;
            node->prev = tail;
            tail = node;
        }
    }
    
    int Q;
    cin >> Q;
    int total = N;
    
    while (Q--) {
        int T, I, X;
        cin >> T >> I >> X;
        
        if (T == 0) {
            total++;
            Node *newNode = new Node(X, total);
            nodes.push_back(newNode);
            
            if (I == 0) {
                newNode->next = head;
                if (head) head->prev = newNode;
                head = newNode;
                if (!tail) tail = newNode;
            } else {
                Node *after = nodes[I];
                newNode->next = after->next;
                newNode->prev = after;
                if (after->next) after->next->prev = newNode;
                after->next = newNode;
                if (after == tail) tail = newNode;
            }
        } else {
            Node *current = nodes[I];
            int targetHeight = current->height + X;
            Node *candidate = current->next;
            int answer = 0;
            
            while (candidate) {
                if (candidate->height > targetHeight) {
                    answer = candidate->idx;
                    break;
                }
                candidate = candidate->next;
            }
            
            cout << answer << '\n';
        }
    }
    
    return 0;
}
