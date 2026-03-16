#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct DSU {
    vector<int> p, sz;
    vector<ll> sum, mn, ans;
    DSU(int n = 0) { init(n); }
    void init(int n) {
        p.resize(n);
        sz.assign(n, 1);
        sum.assign(n, 0);
        mn.assign(n, 0);
        ans.assign(n, -1);
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
        sum[a] += sum[b];
        mn[a] = min(mn[a], mn[b]);
        return a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int V = N * M;

    vector<ll> pwr(V);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> pwr[i * M + j];
        }
    }

    vector<vector<int>> g(V);
    vector<int> indeg(V, 0);

    auto add_edge = [&](int u, int v) {
        if (u == v) return;
        g[u].push_back(v);
        indeg[v]++;
    };

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int u = i * M + j;
            if (i + 1 < N) {
                int v = (i + 1) * M + j;
                if (pwr[u] < pwr[v]) add_edge(u, v);
                else if (pwr[v] < pwr[u]) add_edge(v, u);
            }
            if (j + 1 < M) {
                int v = i * M + (j + 1);
                if (pwr[u] < pwr[v]) add_edge(u, v);
                else if (pwr[v] < pwr[u]) add_edge(v, u);
            }
        }
    }

    queue<int> q;
    for (int i = 0; i < V; ++i) if (indeg[i] == 0) q.push(i);

    vector<int> topo;
    topo.reserve(V);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        topo.push_back(u);
        for (int v : g[u]) {
            if (--indeg[v] == 0) q.push(v);
        }
    }

    DSU dsu(V);
    for (int i = 0; i < V; ++i) {
        dsu.sum[i] = pwr[i];
        dsu.mn[i] = pwr[i];
    }

    vector<char> active(V, 0);

    for (int idx = V - 1; idx >= 0; --idx) {
        int u = topo[idx];
        active[u] = 1;
        int ru = dsu.find(u);

        int x = u / M, y = u % M;
        const int dx[4] = {-1, 1, 0, 0};
        const int dy[4] = {0, 0, -1, 1};

        for (int k = 0; k < 4; ++k) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            int v = nx * M + ny;
            if (!active[v]) continue;
            if (pwr[v] < pwr[u]) continue;
            int rv = dsu.find(v);
            ru = dsu.find(ru);
            if (ru == rv) continue;

            ll need_ru = dsu.mn[ru];
            ll need_rv = dsu.mn[rv];

            bool ru_can_rv = dsu.sum[ru] >= need_rv;
            bool rv_can_ru = dsu.sum[rv] >= need_ru;

            if (ru_can_rv && rv_can_ru) {
                ru = dsu.unite(ru, rv);
            }
        }
    }

    vector<int> roots;
    roots.reserve(V);
    vector<char> seen(V, 0);
    for (int i = 0; i < V; ++i) {
        int r = dsu.find(i);
        if (!seen[r]) {
            seen[r] = 1;
            roots.push_back(r);
        }
    }

    vector<vector<int>> dag(V);
    vector<int> indeg2(V, 0);

    for (int u = 0; u < V; ++u) {
        int ru = dsu.find(u);
        for (int v : g[u]) {
            int rv = dsu.find(v);
            if (ru != rv) {
                dag[ru].push_back(rv);
            }
        }
    }

    for (int r : roots) {
        auto &vec = dag[r];
        sort(vec.begin(), vec.end());
        vec.erase(unique(vec.begin(), vec.end()), vec.end());
        for (int v : vec) indeg2[v]++;
    }

    queue<int> q2;
    for (int r : roots) if (indeg2[r] == 0) q2.push(r);

    vector<int> topo2;
    topo2.reserve(roots.size());
    while (!q2.empty()) {
        int u = q2.front(); q2.pop();
        topo2.push_back(u);
        for (int v : dag[u]) {
            if (--indeg2[v] == 0) q2.push(v);
        }
    }

    for (int idx = (int)topo2.size() - 1; idx >= 0; --idx) {
        int r = topo2[idx];
        ll best = dsu.sum[r];
        for (int v : dag[r]) {
            if (best >= dsu.mn[v]) {
                best = max(best, dsu.ans[v] + dsu.sum[r]);
            }
        }
        dsu.ans[r] = best;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            int id = i * M + j;
            if (j) cout << ' ';
            cout << dsu.ans[dsu.find(id)];
        }
        cout << '\n';
    }

    return 0;
}