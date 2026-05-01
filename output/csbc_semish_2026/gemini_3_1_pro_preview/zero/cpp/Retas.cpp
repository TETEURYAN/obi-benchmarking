
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long y1, y2;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    long long X1, X2;
    if (!(cin >> N >> X1 >> X2)) return 0;
    
    vector<Line> lines(N);
    vector<long long> y2_vals(N);
    for (int i = 0; i < N; ++i) {
        long long A, B;
        cin >> A >> B;
        lines[i].y1 = A * X1 + B;
        lines[i].y2 = A * X2 + B;
        y2_vals[i] = lines[i].y2;
    }
    
    sort(lines.begin(), lines.end(), [](const Line& a, const Line& b) {
        if (a.y1 != b.y1)
            return a.y1 < b.y1;
        return a.y2 > b.y2;
    });
    
    sort(y2_vals.begin(), y2_vals.end());
    y2_vals.erase(unique(y2_vals.begin(), y2_vals.end()), y2_vals.end());
    int K = y2_vals.size();
    
    vector<int> bit(K + 1, 0);
    auto add = [&](int idx, int val) {
        for (; idx <= K; idx += idx & -idx)
            bit[idx] += val;
    };
    
    auto query = [&](int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx)
            sum += bit[idx];
        return sum;
    };
    
    long long intersections = 0;
    for (int i = 0; i < N; ++i) {
        int rank = lower_bound(y2_vals.begin(), y2_vals.end(), lines[i].y2) - y2_vals.begin() + 1;
        intersections += i - query(rank - 1);
        add(rank, 1);
    }
    
    cout << intersections << "\n";
    return 0;
}
