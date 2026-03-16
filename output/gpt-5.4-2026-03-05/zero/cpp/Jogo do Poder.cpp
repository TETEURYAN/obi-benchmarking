#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, sz;
    vector<long long> sum;
    DSU(int n = 0) { init(n); }
    void init(int n) {
        p.resize(n);
        sz.assign(n, 1);
        sum.assign(n, 0);
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
        return a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int K = N * M;

    vector<long long> val(K);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> val[i * M + j];
        }
    }

    vector<int> ord(K);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) {
        if (val[a] != val[b]) return val[a] < val[b];
        return a < b;
    });

    DSU dsu(K);
    for (int i = 0; i < K; ++i) dsu.sum[i] = val[i];

    vector<char> active(K, 0);
    vector<vector<int>> members(K);
    vector<long long> ans(K, -1);

    auto add_member = [&](int root, int v) {
        members[root].push_back(v);
    };

    int ptr = 0;
    while (ptr < K) {
        int q = ptr;
        long long w = val[ord[ptr]];
        while (q < K && val[ord[q]] == w) q++;

        for (int t = ptr; t < q; ++t) {
            int v = ord[t];
            active[v] = 1;
            members[v].push_back(v);

            int r = v / M, c = v % M;
            if (r > 0) {
                int u = v - M;
                if (active[u]) {
                    int a = dsu.find(v), b = dsu.find(u);
                    if (a != b) {
                        int nr = dsu.unite(a, b);
                        int other = (nr == a ? b : a);
                        if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                        for (int x : members[other]) members[nr].push_back(x);
                        vector<int>().swap(members[other]);
                    }
                }
            }
            if (r + 1 < N) {
                int u = v + M;
                if (active[u]) {
                    int a = dsu.find(v), b = dsu.find(u);
                    if (a != b) {
                        int nr = dsu.unite(a, b);
                        int other = (nr == a ? b : a);
                        if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                        for (int x : members[other]) members[nr].push_back(x);
                        vector<int>().swap(members[other]);
                    }
                }
            }
            if (c > 0) {
                int u = v - 1;
                if (active[u]) {
                    int a = dsu.find(v), b = dsu.find(u);
                    if (a != b) {
                        int nr = dsu.unite(a, b);
                        int other = (nr == a ? b : a);
                        if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                        for (int x : members[other]) members[nr].push_back(x);
                        vector<int>().swap(members[other]);
                    }
                }
            }
            if (c + 1 < M) {
                int u = v + 1;
                if (active[u]) {
                    int a = dsu.find(v), b = dsu.find(u);
                    if (a != b) {
                        int nr = dsu.unite(a, b);
                        int other = (nr == a ? b : a);
                        if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                        for (int x : members[other]) members[nr].push_back(x);
                        vector<int>().swap(members[other]);
                    }
                }
            }
        }

        unordered_set<int> roots;
        roots.reserve((q - ptr) * 2 + 1);
        for (int t = ptr; t < q; ++t) roots.insert(dsu.find(ord[t]));

        bool changed = true;
        while (changed) {
            changed = false;
            vector<int> process_roots;
            process_roots.reserve(roots.size());
            for (int r : roots) {
                if (dsu.find(r) == r) process_roots.push_back(r);
            }
            roots.clear();
            for (int r : process_roots) {
                long long s = dsu.sum[r];
                if (s >= w) {
                    changed = true;
                    vector<int> cur = move(members[r]);
                    for (int x : cur) {
                        if (ans[x] == -1) ans[x] = s;
                        int rr = x / M, cc = x % M;
                        if (rr > 0) {
                            int y = x - M;
                            if (active[y]) {
                                int a = dsu.find(x), b = dsu.find(y);
                                if (a != b) {
                                    int nr = dsu.unite(a, b);
                                    int other = (nr == a ? b : a);
                                    if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                                    for (int z : members[other]) members[nr].push_back(z);
                                    vector<int>().swap(members[other]);
                                }
                            }
                        }
                        if (rr + 1 < N) {
                            int y = x + M;
                            if (active[y]) {
                                int a = dsu.find(x), b = dsu.find(y);
                                if (a != b) {
                                    int nr = dsu.unite(a, b);
                                    int other = (nr == a ? b : a);
                                    if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                                    for (int z : members[other]) members[nr].push_back(z);
                                    vector<int>().swap(members[other]);
                                }
                            }
                        }
                        if (cc > 0) {
                            int y = x - 1;
                            if (active[y]) {
                                int a = dsu.find(x), b = dsu.find(y);
                                if (a != b) {
                                    int nr = dsu.unite(a, b);
                                    int other = (nr == a ? b : a);
                                    if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                                    for (int z : members[other]) members[nr].push_back(z);
                                    vector<int>().swap(members[other]);
                                }
                            }
                        }
                        if (cc + 1 < M) {
                            int y = x + 1;
                            if (active[y]) {
                                int a = dsu.find(x), b = dsu.find(y);
                                if (a != b) {
                                    int nr = dsu.unite(a, b);
                                    int other = (nr == a ? b : a);
                                    if (members[nr].size() < members[other].size()) members[nr].swap(members[other]);
                                    for (int z : members[other]) members[nr].push_back(z);
                                    vector<int>().swap(members[other]);
                                }
                            }
                        }
                    }
                    int nr = dsu.find(r);
                    roots.insert(nr);
                } else {
                    roots.insert(r);
                }
            }
        }

        ptr = q;
    }

    for (int i = 0; i < K; ++i) {
        if (ans[i] == -1) ans[i] = val[i];
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (j) cout << ' ';
            cout << ans[i * M + j];
        }
        cout << '\n';
    }

    return 0;
}