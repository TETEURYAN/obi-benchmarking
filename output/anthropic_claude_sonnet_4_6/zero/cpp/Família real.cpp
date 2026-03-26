
#include<bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    
    vector<int> parent(N+1);
    for(int i = 1; i <= N; i++){
        cin >> parent[i];
    }
    
    // BFS to find generation of each descendant
    // King is 0, generation 1 = children of king
    vector<int> gen(N+1, 0);
    
    // Find generation using parent info
    // gen[i] = gen[parent[i]] + 1, gen of king's children = 1
    // We need to compute gen for all, but parent might not be in order
    // Use memoization/recursion or topological order
    
    // Since parent[i] < i is not guaranteed, use recursive with memo
    // Actually let's do iterative with a queue
    
    // First, find all nodes whose parent is 0 (king)
    // gen[i] = gen[parent[i]] + 1
    // gen[0] = 0 (king)
    
    vector<int> genArr(N+1, -1);
    genArr[0] = 0; // king
    
    // Compute gen for all descendants
    // Use DFS/BFS from king
    // Build adjacency list (children)
    vector<vector<int>> children(N+1);
    for(int i = 1; i <= N; i++){
        children[parent[i]].push_back(i);
    }
    
    queue<int> q;
    q.push(0);
    while(!q.empty()){
        int node = q.front(); q.pop();
        for(int child : children[node]){
            genArr[child] = genArr[node] + 1;
            q.push(child);
        }
    }
    
    // Count total per generation and attended per generation
    map<int,int> total, attended;
    for(int i = 1; i <= N; i++){
        total[genArr[i]]++;
    }
    
    set<int> attendedSet;
    for(int i = 0; i < M; i++){
        int x; cin >> x;
        attendedSet.insert(x);
    }
    
    for(int i = 1; i <= N; i++){
        if(attendedSet.count(i)){
            attended[genArr[i]]++;
        }
    }
    
    // Find max generation
    int maxGen = 0;
    for(int i = 1; i <= N; i++){
        maxGen = max(maxGen, genArr[i]);
    }
    
    cout << fixed << setprecision(2);
    for(int g = 1; g <= maxGen; g++){
        double pct = 0.0;
        if(total[g] > 0){
            pct = 100.0 * attended[g] / total[g];
        }
        if(g > 1) cout << " ";
        cout << pct;
    }
    cout << endl;
    
    return 0;
}
