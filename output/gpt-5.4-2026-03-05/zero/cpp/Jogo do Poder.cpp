#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct DSU {
    int n;
    vector<int> p, sz;
    vector<ll> sum, mn, ans;
    vector<vector<int>> members;
    DSU(int n=0): n(n), p(n), sz(n,1), sum(n), mn(n), ans(n,-1), members(n) {
        iota(p.begin(), p.end(), 0);
    }
    int find(int x){
        while(p[x]!=x){
            p[x]=p[p[x]];
            x=p[x];
        }
        return x;
    }
    int unite(int a, int b){
        a=find(a); b=find(b);
        if(a==b) return a;
        if(sz[a]<sz[b]) swap(a,b);
        p[b]=a;
        sz[a]+=sz[b];
        sum[a]+=sum[b];
        mn[a]=min(mn[a], mn[b]);
        if(members[a].size() < members[b].size()) members[a].swap(members[b]);
        members[a].insert(members[a].end(), members[b].begin(), members[b].end());
        vector<int>().swap(members[b]);
        return a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    int V = N * M;

    vector<ll> val(V);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> val[i * M + j];
        }
    }

    vector<int> ord(V);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b){
        if (val[a] != val[b]) return val[a] < val[b];
        return a < b;
    });

    DSU dsu(V);
    for (int i = 0; i < V; ++i) {
        dsu.sum[i] = val[i];
        dsu.mn[i] = val[i];
        dsu.members[i].push_back(i);
    }

    vector<char> active(V, 0);

    auto try_finalize = [&](int r) {
        r = dsu.find(r);
        if (dsu.ans[r] != -1) return;
        if (dsu.sum[r] >= dsu.mn[r] * 2) {
            ll finalSum = dsu.sum[r];
            for (int x : dsu.members[r]) dsu.ans[x] = finalSum;
        }
    };

    int ptr = 0;
    while (ptr < V) {
        int q = ptr;
        ll cur = val[ord[ptr]];
        while (q < V && val[ord[q]] == cur) q++;

        for (int k = ptr; k < q; ++k) {
            int u = ord[k];
            active[u] = 1;
        }

        for (int k = ptr; k < q; ++k) {
            int u = ord[k];
            int i = u / M, j = u % M;
            if (i > 0) {
                int v = u - M;
                if (active[v]) dsu.unite(u, v);
            }
            if (i + 1 < N) {
                int v = u + M;
                if (active[v]) dsu.unite(u, v);
            }
            if (j > 0) {
                int v = u - 1;
                if (active[v]) dsu.unite(u, v);
            }
            if (j + 1 < M) {
                int v = u + 1;
                if (active[v]) dsu.unite(u, v);
            }
        }

        unordered_set<int> roots;
        roots.reserve((q - ptr) * 2 + 1);
        for (int k = ptr; k < q; ++k) roots.insert(dsu.find(ord[k]));
        for (int r : roots) try_finalize(r);

        ptr = q;
    }

    for (int i = 0; i < V; ++i) {
        if (dsu.ans[i] == -1) dsu.ans[i] = val[i];
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (j) cout << ' ';
            cout << dsu.ans[i * M + j];
        }
        cout << '\n';
    }

    return 0;
}