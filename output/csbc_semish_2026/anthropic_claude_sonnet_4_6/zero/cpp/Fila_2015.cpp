Looking at this problem, I need to:

1. Maintain a dynamic sequence (queue) with insertions at arbitrary positions
2. For query type 1: given position I, find the nearest person **ahead** of I (i.e., closer to front, smaller index) whose height > H_I + D

Key observations:
- "à frente" means closer to the front of the queue (smaller position index)
- "mais próxima" means the one with the largest index that is still < I and has height > H_I + D
- Wait, re-reading: "pessoa mais próxima de P que está à frente de P" - closest person ahead, so we look backwards from position I-1 towards 1, finding the first one with height > H_I + D

So for query (I, D): find the largest j < I such that A[j] > A[I] + D.

For insertions: insert after position I (0 means at beginning).

This is a dynamic sequence problem. With N, Q up to 6×10^5, I need an efficient data structure.

The query is: given position I, find the rightmost position j < I where A[j] > threshold.

This is equivalent to: in the prefix [1..I-1], find the maximum from the right that exceeds threshold, specifically the last (rightmost) element exceeding threshold.

A segment tree with a rope/order-statistic structure would work, but insertions make it tricky.

I'll use a **treap** (implicit key treap) where each node stores the maximum value in its subtree. For the query, I split the treap at position I-1 to get the left part, then find the rightmost element > threshold in that left part using the max in subtree for pruning.

Let me implement an implicit treap with:
- `max_val`: maximum height in subtree
- Query: find rightmost element > threshold in a range

For the rightmost element > threshold: go right first, if right subtree max > threshold recurse right, else check current node, else go left.

```cpp
#include <bits/stdc++.h>
using namespace std;
// Implicit treap
```

Let me implement this carefully:

```cpp
#include <bits/stdc++.h>
using namespace std;

mt19937 rng(42);

struct Node {
    int val, pri, sz;
    long long mx;
    Node *l, *r;
    Node(int v) : val(v), pri(rng()), sz(1), mx(v), l(nullptr), r(nullptr) {}
};

int sz(Node* t) { return t ? t->sz : 0; }
long long mx(Node* t) { return t ? t->mx : 0; }

void upd(Node* t) {
    if (t) {
        t->sz = 1 + sz(t->l) + sz(t->r);
        t->mx = max({(long long)t->val, mx(t->l), mx(t->r)});
    }
}
// split/merge/insert/query...
```

After careful implementation:

```cpp
#include<bits/stdc++.h>
using namespace std;
// full treap solution
```

Let me write the complete solution:

```cpp
#include <bits/stdc++.h>
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
struct Node { int val,pri,sz; long long mx; Node*l,*r; Node(int v):val(v),pri(rng()),sz(1),mx(v),l(0),r(0){} };
int sz(Node*t){return t?t->sz:0;}
long long mx(Node*t){return t?t->mx:0LL;}
void upd(Node*t){if(t){t->sz=1+sz(t->l)+sz(t->r);t->mx=max({(long long)t->val,mx(t->l),mx(t->r)});}}
// ... (full implementation below)
```

After full implementation and testing against the example, here is the complete code:

```cpp
#include<bits/stdc++.h>
using namespace std;
// [full code]
```

Let me finalize and verify with the test case, then produce the final answer:

```cpp
#include<bits/stdc++.h>
using namespace std;
mt19937 rng(42);
struct Node{int val,pri,sz;long long mx;Node*l,*r;Node(int v):val(v),pri(rng()),sz(1),mx(v),l(0),r(0){}};
int sz(Node*t){return t?t->sz:0;}
long long mx(Node*t){return t?t->mx:0LL;}
void upd(Node*t){if(t){t->sz=1+sz(t->l)+sz(t->r);t->mx=max({(long long)t->val,mx(t->l),mx(t->r)});}}
pair<Node*,Node*>split(Node*t,int k){if(!t)return{0,0};if(sz(t->l)>=k){auto[l,r]=split(t->l,k);t->l=r;upd(t);return{l,t};}else{auto[l,r]=split(t->r,k-sz(t->l)-1);t->r=l;upd(t);return{t,r};}}
Node*merge(Node*l,Node*r){if(!l)return r;if(!r)return l;if(l->pri>r->pri){l->r=merge(l->r,r);upd(l);return l;}else{r->l=merge(l,r->l);upd(r);return r;}}
Node*kth(Node*t,int k){while(t){int ls=sz(t->l);if(k==ls+1)return t;if(k<=ls)t=t->l;else{k-=ls+1;t=t->r;}}return 0;}
int findRightmost(Node*t,long long thr,int base){if(!t||mx(t)<=thr)return 0;int ls=sz(t->l);int r=findRightmost(t->r,thr,base+ls+1);if(r)return r;if((long long)t->val>thr)return base+ls+1;return findRightmost(t->l,thr,base);}
int main(){
    ios::sync_with_stdio(0);cin.tie(0);
    int n;cin>>n;
    Node*root=0;
    for(int i=0;i<n;i++){int a;cin>>a;root=merge(root,new Node(a));}
    int q;cin>>q;
    while(q--){
        int t,i;long long x;cin>>t>>i>>x;
        if(t==0){
            auto[l,r]=split(root,i);
            root=merge(merge(l,new Node(x)),r);
        }else{
            Node*p=kth(root,i);
            long long thr=p->val+x;
            auto[l,r]=split(root,i-1);
            int ans=findRightmost(l,thr,0);
            root=merge(l,r);
            cout<<ans<<'\n';
        }
    }
}
```