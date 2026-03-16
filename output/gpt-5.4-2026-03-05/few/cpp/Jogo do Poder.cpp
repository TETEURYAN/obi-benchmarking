#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, sz;
    DSU(int n = 0) { init(n); }
    void init(int n) {
        p.resize(n);
        sz.assign(n, 1);
        iota(p.begin(), p.end(), 0);
    }
    int find(int x) {
        while (p[x] != x) {
            p[x] = p[p[x]];
            x = p[x];
        }
        return x;
    }
    int unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return a;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
        return a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;
    int K = N * M;

    vector<long long> P(K);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> P[i * M + j];
        }
    }

    vector<vector<int>> byValue;
    {
        vector<long long> vals = P;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        byValue.assign(vals.size(), {});
        for (int i = 0; i < K; i++) {
            int id = lower_bound(vals.begin(), vals.end(), P[i]) - vals.begin();
            byValue[id].push_back(i);
        }

        DSU dsu(K);
        vector<char> active(K, 0);
        vector<long long> compSum(K, 0);
        vector<long long> compNeed(K, 0);
        vector<vector<int>> members(K);
        vector<long long> ans(K, -1);

        auto try_finalize = [&](int root) {
            root = dsu.find(root);
            if (compNeed[root] == -1) return;
            if (compSum[root] >= compNeed[root]) {
                long long finalSum = compSum[root];
                queue<int> q;
                q.push(root);
                compNeed[root] = -1;
                while (!q.empty()) {
                    int r = q.front();
                    q.pop();
                    for (int v : members[r]) ans[v] = finalSum;
                }
            }
        };

        for (int gid = 0; gid < (int)vals.size(); gid++) {
            long long curVal = vals[gid];

            for (int v : byValue[gid]) {
                active[v] = 1;
                dsu.p[v] = v;
                dsu.sz[v] = 1;
                compSum[v] = P[v];
                compNeed[v] = 2 * P[v];
                members[v].clear();
                members[v].push_back(v);
            }

            for (int v : byValue[gid]) {
                int x = v / M, y = v % M;
                const int dx[4] = {-1, 1, 0, 0};
                const int dy[4] = {0, 0, -1, 1};
                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d], ny = y + dy[d];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
                    int u = nx * M + ny;
                    if (!active[u]) continue;
                    int a = dsu.find(v), b = dsu.find(u);
                    if (a == b) continue;

                    int nr = dsu.unite(a, b);
                    int oroot = (nr == a ? b : a);

                    compSum[nr] = compSum[a] + compSum[b];

                    long long needA = compNeed[a];
                    long long needB = compNeed[b];
                    if (needA == -1 || needB == -1) compNeed[nr] = -1;
                    else compNeed[nr] = min(needA, needB);

                    if (members[nr].size() < members[oroot].size()) {
                        members[nr].swap(members[oroot]);
                    }
                    for (int node : members[oroot]) members[nr].push_back(node);
                    vector<int>().swap(members[oroot]);
                }
            }

            unordered_set<int> roots;
            roots.reserve(byValue[gid].size() * 2 + 1);
            for (int v : byValue[gid]) roots.insert(dsu.find(v));
            for (int r : roots) try_finalize(r);
        }

        for (int i = 0; i < K; i++) {
            if (ans[i] == -1) ans[i] = P[i];
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (j) cout << ' ';
                cout << ans[i * M + j];
            }
            cout << '\n';
        }
    }

    return 0;
}