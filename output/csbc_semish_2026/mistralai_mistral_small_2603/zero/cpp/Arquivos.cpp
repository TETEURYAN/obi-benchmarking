
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long B;
    cin >> N >> B;

    vector<long long> files(N);
    for (int i = 0; i < N; ++i) {
        cin >> files[i];
    }

    sort(files.begin(), files.end());

    int left = 0;
    int right = N - 1;
    int folders = 0;

    while (left <= right) {
        if (files[left] + files[right] <= B) {
            left++;
            right--;
        } else {
            right--;
        }
        folders++;
    }

    cout << folders << '\n';
    return 0;
}
