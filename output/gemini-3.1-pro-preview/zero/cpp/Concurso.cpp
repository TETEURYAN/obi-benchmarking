
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (cin >> n >> k) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        sort(a.rbegin(), a.rend());

        if (k > 0) {
            cout << a[k - 1] << "\n";
        } else {
            cout << 100 << "\n";
        }
    }

    return 0;
}
