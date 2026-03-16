#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, sz;
    vector<long long> sum;
    DSU() {}
    DSU(int n, const vector<long long>& w) {
        p.resize(n);
        sz.assign(n, 1);
        sum = w;
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
        a = find(a);
        b = find(b);
        if (a == b) return a;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
        sum[a] += sum[b];
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
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> P[i * M + j];
        }
    }

    vector<int> ord(K);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) {
        if (P[a] != P[b]) return P[a] < P[b];
        return a < b;
    });

    DSU dsu(K, P);
    vector<char> active(K, 0);
    vector<long long> ans(K, -1);

    auto try_union = [&](int u, int v) {
        if (!active[v]) return;
        int ru = dsu.find(u), rv = dsu.find(v);
        if (ru == rv) return;
        dsu.unite(ru, rv);
    };

    int ptr = 0;
    while (ptr < K) {
        int l = ptr;
        long long val = P[ord[ptr]];
        while (ptr < K && P[ord[ptr]] == val) ptr++;
        int r = ptr;

        for (int t = l; t < r; ++t) {
            int u = ord[t];
            active[u] = 1;
        }

        for (int t = l; t < r; ++t) {
            int u = ord[t];
            int x = u / M, y = u % M;
            if (x > 0) try_union(u, u - M);
            if (x + 1 < N) try_union(u, u + M);
            if (y > 0) try_union(u, u - 1);
            if (y + 1 < M) try_union(u, u + 1);
        }

        unordered_map<int, vector<int>> groups;
        groups.reserve((r - l) * 2 + 1);
        for (int t = l; t < r; ++t) {
            int u = ord[t];
            groups[dsu.find(u)].push_back(u);
        }

        queue<int> q;
        for (auto &it : groups) {
            int root = it.first;
            if (ans[root] != -1) continue;
            if (dsu.sum[root] >= val) {
                ans[root] = dsu.sum[root];
                q.push(root);
            }
        }

        while (!q.empty()) {
            int root = q.front();
            q.pop();
            long long cur = ans[root];
            for (int u : groups[root]) {
                int x = u / M, y = u % M;
                if (x > 0) {
                    int v = u - M;
                    if (active[v]) {
                        int rv = dsu.find(v);
                        if (rv != root && ans[rv] == -1 && cur >= P[rv]) {
                            ans[rv] = cur + dsu.sum[rv];
                            q.push(rv);
                        }
                    }
                }
                if (x + 1 < N) {
                    int v = u + M;
                    if (active[v]) {
                        int rv = dsu.find(v);
                        if (rv != root && ans[rv] == -1 && cur >= P[rv]) {
                            ans[rv] = cur + dsu.sum[rv];
                            q.push(rv);
                        }
                    }
                }
                if (y > 0) {
                    int v = u - 1;
                    if (active[v]) {
                        int rv = dsu.find(v);
                        if (rv != root && ans[rv] == -1 && cur >= P[rv]) {
                            ans[rv] = cur + dsu.sum[rv];
                            q.push(rv);
                        }
                    }
                }
                if (y + 1 < M) {
                    int v = u + 1;
                    if (active[v]) {
                        int rv = dsu.find(v);
                        if (rv != root && ans[rv] == -1 && cur >= P[rv]) {
                            ans[rv] = cur + dsu.sum[rv];
                            q.push(rv);
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < K; ++i) {
        int r = dsu.find(i);
        if (ans[r] == -1) ans[r] = dsu.sum[r];
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (j) cout << ' ';
            cout << ans[dsu.find(i * M + j)];
        }
        cout << '\n';
    }

    return 0;
}