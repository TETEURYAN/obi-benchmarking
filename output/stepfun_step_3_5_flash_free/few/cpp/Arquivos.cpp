#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    long long B;
    if (!(cin >> N >> B)) return 0;

    vector<long long> files(N);
    for (int i = 0; i < N; i++) {
        cin >> files[i];
    }

    sort(files.begin(), files.end());

    int i = 0, j = N - 1;
    int folders = 0;

    while (i <= j) {
        if (i == j) {
            folders++;
            break;
        }
        if (files[i] + files[j] <= B) {
            i++;
            j--;
            folders++;
        } else {
            j--;
            folders++;
        }
    }

    cout << folders << endl;
    return 0;
}