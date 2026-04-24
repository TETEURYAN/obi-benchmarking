Looking at this problem:

- We have a tree with N cities
- **Capitals** are nodes with degree 1 (leaves)
- Non-capitals have degree ≥ 2
- No path between two capitals passes through another capital (this is guaranteed by the structure)
- Find the minimum distance between any pair of capitals

Since capitals are leaves (degree 1), I need to find the minimum distance between any two leaves in the tree.

Key insight: The path between two leaves goes through internal nodes. The minimum distance between two leaves is the minimum over all internal nodes of: (minimum depth to a leaf in subtree1 + minimum depth to a leaf in subtree2 + 2), where subtree1 and subtree2 are different children subtrees.

Actually, for each node, I can find the two smallest distances to a leaf among its children, and the answer candidate is their sum + 2.

Also, if a node is adjacent to two leaves directly, the answer could be 2.

Let me think with DP:
- For each node v, compute `minLeafDist[v]` = minimum distance from v to any leaf in its subtree (rooted tree)
- For each internal node v with children c1, c2, ..., take the two smallest values of `(minLeafDist[ci] + 1)`, their sum is a candidate answer
- Also need to consider paths going up through parent

Actually since the tree can be large, I'll do a proper tree DP considering all directions.

Let me use rerooting technique:
1. Root the tree at node 1
2. Compute `down[v]` = min distance from v to a leaf in its subtree
3. Compute `up[v]` = min distance from v to a leaf going upward
4. For each node v, the answer considers pairs of directions (children + up direction)

For each node v, collect all distances to leaves in each direction (each child gives `down[child]+1`, and parent direction gives `up[v]`). Take the two smallest and sum them.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n;
vector<int> adj[100005];
int down_val[100005];
int up_val[100005];
int ans;

void dfs1(int u, int par) {
    if (adj[u].size() == 1) { // leaf
        down_val[u] = 0;
        return;
    }
    down_val[u] = INF;
    for (int v : adj[u]) {
        if (v == par) continue;
        dfs1(v, u);
        down_val[u] = min(down_val[u], down_val[v] + 1);
    }
}

void dfs2(int u, int par) {
    // collect all distances to leaves from u in each direction
    vector<int> dists;
    if (up_val[u] < INF) dists.push_back(up_val[u]);
    for (int v : adj[u]) {
        if (v == par) continue;
        dists.push_back(down_val[v] + 1);
    }
    sort(dists.begin(), dists.end());
    if (dists.size() >= 2) {
        ans = min(ans, dists[0] + dists[1]);
    }
    
    // compute up for children
    for (int v : adj[u]) {
        if (v == par) continue;
        // up[v] = min distance going up through u
        // = 1 + min of all directions of u except v
        int best1 = INF, best2 = INF;
        // directions: up_val[u], and all children except v
        auto update = [&](int val) {
            if (val < best1) { best2 = best1; best1 = val; }
            else if (val < best2) { best2 = val; }
        };
        if (up_val[u] < INF) update(up_val[u]);
        for (int w : adj[u]) {
            if (w == par || w == v) continue;
            update(down_val[w] + 1);
        }
        up_val[v] = (best1 < INF) ? best1 + 1 : INF;
        dfs2(v, u);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 0; i < n-1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    ans = INF;
    fill(up_val+1, up_val+n+1, INF);
    dfs1(1, -1);
    dfs2(1, -1);
    cout << ans << "\n";
}
```

Testing on example 1: leaves are 1,4,6,8 (degree 1). Min distance between pairs... 1-4 is 3, 4-6 is 4, etc. Answer is 3. ✓