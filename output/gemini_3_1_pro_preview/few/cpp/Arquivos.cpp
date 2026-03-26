#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long b;
    if (cin >> n >> b) {
        vector<long long> files(n);
        for (int i = 0; i < n; i++) {
            cin >> files[i];
        }

        sort(files.begin(), files.end());

        int left = 0;
        int right = n - 1;
        int folders = 0;

        while (left <= right) {
            if (left == right) {
                folders++;
                break;
            }
            if (files[left] + files[right] <= b) {
                folders++;
                left++;
                right--;
            } else {
                folders++;
                right--;
            }
        }

        cout << folders << "\n";
    }

    return 0;
}