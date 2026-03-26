#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> seq(n);
    for (int i = 0; i < n; i++) {
        cin >> seq[i];
    }

    int count = 0;
    for (int i = -1; i < n - 2; i++) {
        if (seq[i + 1] == 1 && seq[i + 2] == 0 && seq[i + 3] == 0) {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}