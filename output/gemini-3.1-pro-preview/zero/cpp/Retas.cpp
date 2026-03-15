
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long y1, y2;
};

bool compareLines(const Line& a, const Line& b) {
    if (a.y1 != b.y1)
        return a.y1 < b.y1;
    return a.y2 > b.y2;
}

struct BIT {
    int n;
    vector<int> tree;
    BIT(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i)
            tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i)
            sum += tree[i];
        return sum;
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

    sort(lines.begin(), lines.end(), compareLines);

    sort(y2_vals.begin(), y2_vals.end());
    y2_vals.erase(unique(y2_vals.begin(), y2_vals.end()), y2_vals.end());

    BIT bit(y2_vals.size());
    long long intersections = 0;

    for (int i = 0; i < n; ++i) {
        int rank = lower_bound(y2_vals.begin(), y2_vals.end(), lines[i].y2) - y2_vals.begin() + 1;
        intersections += bit.query(y2_vals.size()) - bit.query(rank - 1);
        bit.add(rank, 1);
    }

    cout << intersections << "\n";

    return 0;
}
