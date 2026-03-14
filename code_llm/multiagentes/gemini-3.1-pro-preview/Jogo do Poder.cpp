#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Cell {
    int r, c;
    long long p;
    int id;
    bool operator<(const Cell& other) const {
        return p < other.p;
    }
};

int N, M;
vector<long long> P_flat;
vector<int> parent_node;
vector<long long> sum_power;
vector<vector<int>> adj;
vector<long long> ans;

int find_set(int v) {
    if (v == parent_node[v])
        return v;
    return parent_node[v] = find_set(parent_node[v]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    if (!(cin >> N >> M)) return 0;
    
    int K = N * M;
    P_flat.resize(K);
    parent_node.resize(K);
    sum_power.resize(K);
    adj.resize(K);
    ans.resize(K);
    
    vector<Cell> cells(K);
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < M; ++j) {
            long long p;
            cin >> p;
            int id = i * M + j;
            P_flat[id] = p;
            cells[id] = {i, j, p, id};
            parent_node[id] = id;
            sum_power[id] = p;
        }
    }
    
    sort(cells.begin(), cells.end());
    
    vector<bool> processed(K, false);
    
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};
    
    for(int i = 0; i < K; ++i) {
        int u = cells[i].id;
        processed[u] = true;
        
        int r = cells[i].r;
        int c = cells[i].c;
        
        for(int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            
            if(nr >= 0 && nr < N && nc >= 0 && nc < M) {
                int v = nr * M + nc;
                if(processed[v]) {
                    int root_v = find_set(v);
                    if(root_v != u) {
                        parent_node[root_v] = u;
                        adj[u].push_back(root_v);
                        sum_power[u] += sum_power[root_v];
                    }
                }
            }
        }
    }
    
    vector<pair<int, long long>> q;
    q.reserve(K);
    for(int i = 0; i < K; ++i) {
        if(parent_node[i] == i) {
            q.push_back({i, sum_power[i]});
        }
    }
    
    int head = 0;
    while(head < (int)q.size()) {
        int u = q[head].first;
        long long current_ans = q[head].second;
        head++;
        
        ans[u] = current_ans;
        for(int v : adj[u]) {
            if(sum_power[v] >= P_flat[u]) {
                q.push_back({v, current_ans});
            } else {
                q.push_back({v, sum_power[v]});
            }
        }
    }
    
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < M; ++j) {
            cout << ans[i * M + j] << (j == M - 1 ? "" : " ");
        }
        cout << "\n";
    }
    
    return 0;
}