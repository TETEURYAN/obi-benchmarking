
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long b;
    if (!(cin >> n >> b)) return 0;

    vector<long long> files(n);
    for (int i = 0; i < n; ++i) {
        cin >> files[i];
    }

    sort(files.begin(), files.end());

    int i = 0;
    int j = n - 1;
    int folders = 0;

    while (i <= j) {
        if (i == j) {
            folders++;
            break;
        }
        if (files[i] + files[j] <= b) {
            folders++;
            i++;
            j--;
        } else {
            folders++;
            j--;
        }
    }

    cout << folders << "\n";

    return 0;
}
