#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long merge_count(vector<long long>& A, vector<long long>& temp, int l, int r) {
    if (l >= r) return 0;
    int m = l + (r - l) / 2;
    long long inv = merge_count(A, temp, l, m) + merge_count(A, temp, m + 1, r);
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (A[i] < A[j]) {
            temp[k++] = A[i++];
        } else {
            inv += (m - i + 1);
            temp[k++] = A[j++];
        }
    }
    while (i <= m) temp[k++] = A[i++];
    while (j <= r) temp[k++] = A[j++];
    for (int p = l; p <= r; p++) A[p] = temp[p];
    return inv;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    long long X1, X2;
    if (!(cin >> N >> X1 >> X2)) return 0;
    
    vector<pair<long long, long long>> lines(N);
    for (int i = 0; i < N; i++) {
        long long A, B;
        cin >> A >> B;
        long long y1 = A * X1 + B;
        long long y2 = A * X2 + B;
        lines[i] = {y1, y2};
    }
    
    sort(lines.begin(), lines.end(), [](const pair<long long, long long>& a, const pair<long long, long long>& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second;
    });
    
    vector<long long> Y2(N);
    for (int i = 0; i < N; i++) {
        Y2[i] = lines[i].second;
    }
    
    vector<long long> temp(N);
    cout << merge_count(Y2, temp, 0, N - 1) << "\n";
    
    return 0;
}