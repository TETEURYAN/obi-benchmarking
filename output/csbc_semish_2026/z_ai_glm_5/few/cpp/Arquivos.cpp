#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long b;
    if (!(cin >> n >> b)) return 0;

    vector<long long> files(n);
    for (int i = 0; i < n; i++) {
        cin >> files[i];
    }

    sort(files.begin(), files.end());

    int left = 0;
    int right = n - 1;
    int folders = 0;

    while (left <= right) {
        if (files[left] + files[right] <= b) {
            left++;
        }
        right--;
        folders++;
    }

    cout << folders << endl;

    return 0;
}