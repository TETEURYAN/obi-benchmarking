#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    vector<vector<int>> adj(n+1);
    vector<int> deg(n+1, 0);
    
    for(int i = 0; i < n-1; i++){
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
    
    // Capitals are leaves (degree == 1)
    // Non-capitals have degree >= 2
    // We need minimum distance between any pair of capitals
    // Since no path between two capitals passes through another capital,
    // the path between two capitals goes through their non-capital neighbors.
    
    // The minimum distance between two capitals:
    // Each capital is a leaf. The path between two leaves goes through internal nodes.
    // We want the minimum over all pairs of leaves of their distance.
    
    // Key insight: The minimum distance between two leaves is achieved by
    // two leaves that share the same internal neighbor (distance 2),
    // OR if no internal node has degree >= 3 (i.e., it's a path), 
    // then we need to find adjacent leaves or leaves 2 apart.
    
    // Actually: if any internal node has degree >= 3, then there are at least 2 leaf neighbors
    // at distance 2. But internal nodes might not have direct leaf neighbors.
    
    // Better approach: BFS/DFS from each leaf is too slow for N=1e5.
    // 
    // The minimum distance between two leaves in a tree:
    // - If two leaves share the same parent (internal node), distance = 2
    // - Otherwise we need to find the minimum path
    //
    // The minimum distance between any two leaves can be found by:
    // For each internal node, if it has >= 2 leaf children, answer candidate = 2
    // Otherwise, we need to consider paths through the tree.
    //
    // Actually the answer is at least 2 (since leaves can't be adjacent to each other
    // because that would mean both have degree 1 and N=2 special case).
    // Wait, N=2: both nodes have degree 1, they are both capitals, distance=1.
    
    if(n == 2){
        cout << 1 << endl;
        return 0;
    }
    
    // For each internal node, count how many leaf neighbors it has.
    // If any internal node has >= 2 leaf neighbors, answer = 2.
    // Otherwise, we need to find minimum distance.
    // 
    // If no internal node has 2 leaf neighbors, then each internal node has at most 1 leaf neighbor.
    // The tree of internal nodes forms a subtree. We need min distance between two leaves
    // which equals 2 + (distance between their internal neighbors in the internal subtree).
    // Min distance in internal subtree between two nodes that each have a leaf attached = 
    // we need the two closest such nodes in the internal tree.
    // That minimum distance >= 1, so answer >= 3.
    // 
    // To find min distance between internal nodes that have leaf neighbors:
    // BFS/DFS on the internal subtree.
    
    // Check if any internal node has >= 2 leaf neighbors
    for(int v = 1; v <= n; v++){
        if(deg[v] >= 2){ // internal node
            int leafCount = 0;
            for(int u : adj[v]){
                if(deg[u] == 1) leafCount++;
            }
            if(leafCount >= 2){
                cout << 2 << endl;
                return 0;
            }
        }
    }
    
    // No internal node has 2 leaf neighbors.
    // Find minimum distance between internal nodes that have exactly 1 leaf neighbor.
    // BFS from all such nodes simultaneously (multi-source BFS) on internal subgraph.
    
    vector<int> dist(n+1, -1);
    deque<int> q;
    
    // Sources: internal nodes with a leaf neighbor
    for(int v = 1; v <= n; v++){
        if(deg[v] >= 2){
            for(int u : adj[v]){
                if(deg[u] == 1){
                    dist[v] = 0;
                    q.push_back(v);
                    break;
                }
            }
        }
    }
    
    int ans = INT_MAX;
    
    while(!q.empty()){
        int v = q.front(); q.pop_front();
        for(int u : adj[v]){
            if(deg[u] == 1) continue; // skip leaves
            if(dist[u] == -1){
                dist[u] = dist[v] + 1;
                q.push_back(u);
            } else if(dist[u] != dist[v]){ // different source
                // but we can't distinguish sources easily
                // Instead: when we meet a node already visited with different dist
                // Actually multi-source BFS: when we find a node already visited,
                // the distance between two sources through this node is dist[v]+dist[u]+1
                ans = min(ans, dist[v] + dist[u] + 1);
            }
        }
    }
    
    // ans is distance between internal nodes, actual distance between capitals = ans + 2
    if(ans == INT_MAX){
        // Only one internal node has leaf neighbor? Shouldn't happen if n>=3 and tree valid
        cout << -1 << endl;
    } else {
        cout << ans + 2 << endl;
    }
    
    return 0;
}