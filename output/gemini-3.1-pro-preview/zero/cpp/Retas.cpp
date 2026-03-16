
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long y1, y2;
    bool operator<(const Line& other) const {
        if (y1 != other.y1) return y1 < other.y1;
        return y2 > other.y2;
    }
};

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for(; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for(; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    int query(int l, int r) {
        if(l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    long long x1, x2;
    if (!(cin >> n >> x1 >> x2)) return 0;
    
    vector<Line> lines(n);
    vector<long long> y2_vals(n);
    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        lines[i].y1 = a * x1 + b;
        lines[i].y2 = a * x2 + b;
        y2_vals[i] = lines[i].y2;
    }
    
    sort(lines.begin(), lines.end());
    
    sort(y2_vals.begin(), y2_vals.end());
    y2_vals.erase(unique(y2_vals.begin(), y2_vals.end()), y2_vals.end());
    
    Fenwick fenwick(y2_vals.size());
    long long ans = 0;
    
    for (int i = 0; i < n; ++i) {
        int r = lower_bound(y2_vals.begin(), y2_vals.end(), lines[i].y2) - y2_vals.begin() + 1;
        ans += fenwick.query(r, y2_vals.size());
        fenwick.add(r, 1);
    }
    
    cout << ans << "\n";
    
    return 0;
}
