#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    long long N, B;
    cin >> N >> B;
    vector<long long> files(N);
    for (auto &x : files) cin >> x;
    sort(files.begin(), files.end());
    long long left = 0, right = N - 1;
    long long count = 0;
    while (left < right) {
        if (files[left] + files[right] <= B) {
            count++;
            left++;
            right--;
        } else {
            count++;
            right--;
        }
    }
    if (left == right) {
        count++;
    }
    cout << count << endl;
    return 0;
}