#include <bits/stdc++.h>

using namespace std;

struct Line {
    long long y1, y2;
    bool operator<(const Line& other) const {
        if (y1 != other.y1) return y1 < other.y1;
        return y2 > other.y2;
    }
};

int tree[100005];
int M;

void add(int idx, int val) {
    while (idx <= M) {
        tree[idx] += val;
        idx += idx & -idx;
    }
}

int query(int idx) {
    int sum = 0;
    while (idx > 0) {
        sum += tree[idx];
        idx -= idx & -idx;
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long x1, x2;
    if (!(cin >> n >> x1 >> x2)) return 0;

    vector<Line> lines(n);
    vector<long long> y2_vals(n);
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        lines[i].y1 = a * x1 + b;
        lines[i].y2 = a * x2 + b;
    }

    sort(lines.begin(), lines.end());

    for (int i = 0; i < n; i++) {
        y2_vals[i] = lines[i].y2;
    }

    vector<long long> unique_y2 = y2_vals;
    sort(unique_y2.begin(), unique_y2.end());
    unique_y2.erase(unique(unique_y2.begin(), unique_y2.end()), unique_y2.end());

    M = unique_y2.size();

    long long total_intersections = 0;
    for (int i = 0; i < n; i++) {
        int rank = lower_bound(unique_y2.begin(), unique_y2.end(), lines[i].y2) - unique_y2.begin() + 1;
        total_intersections += i - query(rank - 1);
        add(rank, 1);
    }

    cout << total_intersections << "\n";

    return 0;
}