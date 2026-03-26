#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    long long B;
    cin >> N >> B;
    vector<long long> files(N);
    for (int i = 0; i < N; i++) {
        cin >> files[i];
    }
    sort(files.begin(), files.end());
    
    int i = 0, j = N - 1;
    int folders = 0;
    while (i < j) {
        if (files[i] + files[j] <= B) {
            folders++;
            i++;
            j--;
        } else {
            folders++;
            j--;
        }
    }
    if (i == j) {
        folders++;
    }
    cout << folders << "\n";
    return 0;
}