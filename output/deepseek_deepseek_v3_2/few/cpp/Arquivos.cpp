#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long b;
    if (!(cin >> n >> b)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int left = 0, right = n - 1;
    int folders = 0;

    while (left <= right) {
        if (left == right) {
            folders++;
            break;
        }
        if (a[left] + a[right] <= b) {
            folders++;
            left++;
            right--;
        } else {
            folders++;
            right--;
        }
    }

    cout << folders << endl;
    return 0;
}