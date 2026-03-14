#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long y1, y2;
    bool operator<(const Line& other) const {
        if (y1 != other.y1)
            return y1 < other.y1;
        return y2 > other.y2;
    }
};

long long merge_sort(vector<long long>& arr, vector<long long>& temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long inv = merge_sort(arr, temp, l, mid) + merge_sort(arr, temp, mid + 1, r);
    
    int i = l, j = mid + 1, k = l;
    
    while (i <= mid && j <= r) {
        if (arr[i] < arr[j]) {
            temp[k++] = arr[i++];
        } else {
            inv += (mid - i + 1);
            temp[k++] = arr[j++];
        }
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    
    for (int p = l; p <= r; p++) {
        arr[p] = temp[p];
    }
    return inv;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    long long x1, x2;
    if (!(cin >> n >> x1 >> x2)) return 0;
    
    vector<Line> lines(n);
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        lines[i].y1 = a * x1 + b;
        lines[i].y2 = a * x2 + b;
    }
    
    sort(lines.begin(), lines.end());
    
    vector<long long> y2(n);
    for (int i = 0; i < n; i++) {
        y2[i] = lines[i].y2;
    }
    
    vector<long long> temp(n);
    long long ans = merge_sort(y2, temp, 0, n - 1);
    
    cout << ans << "\n";
    
    return 0;
}