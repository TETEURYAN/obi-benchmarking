#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> seq(N);
    for (int i = 0; i < N; i++) {
        cin >> seq[i];
    }

    int count = 0;
    for (int i = 0; i <= N - 3; i++) {
        if (seq[i] == 1 && seq[i+1] == 0 && seq[i+2] == 0) {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}