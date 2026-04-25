#include <bits/stdc++.h>
using namespace std;

struct FastInput {
    static const int BUFSIZE = 1 << 20;
    int idx, size;
    char buf[BUFSIZE];
    FastInput() : idx(0), size(0) {}
    inline char getChar() {
        if (idx >= size) {
            size = (int)fread(buf, 1, BUFSIZE, stdin);
            idx = 0;
            if (size == 0) return 0;
        }
        return buf[idx++];
    }
    template <class T>
    bool readInt(T &out) {
        char c;
        T sign = 1;
        T val = 0;
        c = getChar();
        if (!c) return false;
        while (c != '-' && (c < '0' || c > '9')) {
            c = getChar();
            if (!c) return false;
        }
        if (c == '-') {
            sign = -1;
            c = getChar();
        }
        while (c >= '0' && c <= '9') {
            val = val * 10 + (c - '0');
            c = getChar();
        }
        out = val * sign;
        return true;
    }
};

static const int MAXM = 1200005;
static const int LOG = 21;

int ch[MAXM][2], prio_[MAXM], sz[MAXM];
int h[MAXM];
int mx[MAXM];
int parent_[MAXM];
int root = 0, nodes = 0;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

inline int getsz(int t) { return t ? sz[t] : 0; }
inline int getmx(int t) { return t ? mx[t] : INT_MIN; }

inline void pull(int t) {
    if (!t) return;
    sz[t] = 1 + getsz(ch[t][0]) + getsz(ch[t][1]);
    mx[t] = max(h[t], max(getmx(ch[t][0]), getmx(ch[t][1])));
    if (ch[t][0]) parent_[ch[t][0]] = t;
    if (ch[t][1]) parent_[ch[t][1]] = t;
}

int newNode(int height) {
    ++nodes;
    ch[nodes][0] = ch[nodes][1] = 0;
    prio_[nodes] = (int)rng();
    sz[nodes] = 1;
    h[nodes] = height;
    mx[nodes] = height;
    parent_[nodes] = 0;
    return nodes;
}

void split(int t, int k, int &a, int &b) {
    if (!t) {
        a = b = 0;
        return;
    }
    if (getsz(ch[t][0]) >= k) {
        split(ch[t][0], k, a, ch[t][0]);
        if (ch[t][0]) parent_[ch[t][0]] = t;
        b = t;
        parent_[b] = 0;
        pull(b);
    } else {
        split(ch[t][1], k - getsz(ch[t][0]) - 1, ch[t][1], b);
        if (ch[t][1]) parent_[ch[t][1]] = t;
        a = t;
        parent_[a] = 0;
        pull(a);
    }
}

int merge_(int a, int b) {
    if (!a || !b) {
        int t = a ? a : b;
        if (t) parent_[t] = 0;
        return t;
    }
    if (prio_[a] > prio_[b]) {
        ch[a][1] = merge_(ch[a][1], b);
        if (ch[a][1]) parent_[ch[a][1]] = a;
        pull(a);
        parent_[a] = 0;
        return a;
    } else {
        ch[b][0] = merge_(a, ch[b][0]);
        if (ch[b][0]) parent_[ch[b][0]] = b;
        pull(b);
        parent_[b] = 0;
        return b;
    }
}

int kth(int t, int k) {
    while (t) {
        int ls = getsz(ch[t][0]);
        if (k <= ls) t = ch[t][0];
        else if (k == ls + 1) return t;
        else k -= ls + 1, t = ch[t][1];
    }
    return 0;
}

int getPos(int x) {
    int res = getsz(ch[x][0]) + 1;
    while (parent_[x]) {
        int p = parent_[x];
        if (ch[p][1] == x) res += getsz(ch[p][0]) + 1;
        x = p;
    }
    return res;
}

int rightmostGreater(int t, long long lim) {
    while (t) {
        if (ch[t][1] && (long long)mx[ch[t][1]] > lim) {
            t = ch[t][1];
        } else if ((long long)h[t] > lim) {
            return t;
        } else {
            t = ch[t][0];
        }
    }
    return 0;
}

int main() {
    FastInput in;
    int N;
    if (!in.readInt(N)) return 0;

    for (int i = 1; i <= N; i++) {
        int a;
        in.readInt(a);
        int nd = newNode(a);
        root = merge_(root, nd);
    }

    int Q;
    in.readInt(Q);

    string out;
    out.reserve((size_t)Q * 3);

    for (int qi = 0; qi < Q; qi++) {
        int T, I, X;
        in.readInt(T);
        in.readInt(I);
        in.readInt(X);

        if (T == 0) {
            int a, b;
            split(root, I, a, b);
            int nd = newNode(X);
            root = merge_(merge_(a, nd), b);
        } else {
            int node = kth(root, I);
            long long lim = (long long)h[node] + (long long)X;
            int a, b;
            split(root, I - 1, a, b);
            int ansNode = rightmostGreater(a, lim);
            int ans = ansNode ? getPos(ansNode) : 0;
            root = merge_(a, b);
            out += to_string(ans);
            out += '\n';
        }
    }

    fwrite(out.c_str(), 1, out.size(), stdout);
    return 0;
}