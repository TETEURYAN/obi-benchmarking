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
vector<long long> P;
vector<int> parent_node;
vector<long long> comp_sum;
vector<vector<int>> active;
vector<long long> ans;
vector<bool> processed;

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
    P.resize(K);
    vector<Cell> cells(K);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int id = i * M + j;
            cin >> P[id];
            cells[id] = {i, j, P[id], id};
        }
    }

    sort(cells.begin(), cells.end());

    parent_node.resize(K);
    comp_sum.resize(K);
    active.resize(K);
    ans.resize(K, 0);
    processed.resize(K, false);

    for (int i = 0; i < K; ++i) {
        parent_node[i] = i;
        comp_sum[i] = P[i];
        active[i].push_back(i);
    }

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    for (int i = 0; i < K; ++i) {
        int u = cells[i].id;
        int r = cells[i].r;
        int c = cells[i].c;
        long long p_u = cells[i].p;

        vector<int> unique_roots;
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                int v = nr * M + nc;
                if (processed[v]) {
                    unique_roots.push_back(find_set(v));
                }
            }
        }

        sort(unique_roots.begin(), unique_roots.end());
        unique_roots.erase(unique(unique_roots.begin(), unique_roots.end()), unique_roots.end());

        long long total_sum = p_u;
        for (int U : unique_roots) {
            if (comp_sum[U] < p_u) {
                for (int cell_id : active[U]) {
                    ans[cell_id] = comp_sum[U];
                }
                active[U].clear();
            }
            total_sum += comp_sum[U];
        }

        int largest_root = u;
        for (int U : unique_roots) {
            if (active[U].size() > active[largest_root].size()) {
                largest_root = U;
            }
        }

        for (int U : unique_roots) {
            if (U != largest_root) {
                active[largest_root].insert(active[largest_root].end(), active[U].begin(), active[U].end());
                active[U].clear();
            }
        }
        if (largest_root != u) {
            active[largest_root].insert(active[largest_root].end(), active[u].begin(), active[u].end());
            active[u].clear();
        }

        for (int U : unique_roots) {
            parent_node[U] = largest_root;
        }
        parent_node[u] = largest_root;
        comp_sum[largest_root] = total_sum;

        processed[u] = true;
    }

    for (int i = 0; i < K; ++i) {
        if (parent_node[i] == i) {
            for (int cell_id : active[i]) {
                ans[cell_id] = comp_sum[i];
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cout << ans[i * M + j] << (j == M - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}