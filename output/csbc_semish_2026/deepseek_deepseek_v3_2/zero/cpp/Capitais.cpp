
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<vector<int>> adj;
vector<int> degree;
vector<bool> isCapital;

int bfs(int start, vector<int>& dist) {
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    int farthest = start;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
                if (isCapital[v] && dist[v] > dist[farthest]) {
                    farthest = v;
                }
            }
        }
    }
    return farthest;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    
    adj.resize(N + 1);
    degree.resize(N + 1, 0);
    
    for (int i = 0; i < N - 1; i++) {
        int U, V;
        cin >> U >> V;
        adj[U].push_back(V);
        adj[V].push_back(U);
        degree[U]++;
        degree[V]++;
    }
    
    isCapital.resize(N + 1, false);
    for (int i = 1; i <= N; i++) {
        if (degree[i] == 1) {
            isCapital[i] = true;
        }
    }
    
    vector<int> capitals;
    for (int i = 1; i <= N; i++) {
        if (isCapital[i]) {
            capitals.push_back(i);
        }
    }
    
    if (capitals.size() == 2) {
        cout << "1\n";
        return 0;
    }
    
    vector<int> dist1(N + 1, -1);
    int cap1 = bfs(capitals[0], dist1);
    
    vector<int> dist2(N + 1, -1);
    int cap2 = bfs(cap1, dist2);
    
    vector<int> dist3(N + 1, -1);
    bfs(cap2, dist3);
    
    int minDist = N;
    for (int i = 1; i <= N; i++) {
        if (isCapital[i]) {
            minDist = min(minDist, max(dist2[i], dist3[i]));
        }
    }
    
    cout << minDist << "\n";
    
    return 0;
}
