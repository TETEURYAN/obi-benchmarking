#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_h = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] > max_h) {
            max_h = a[i];
        }
    }

    long long ans = 0;
    int prev = max_h;
    
    for (int i = 0; i < n; ++i) {
        if (prev > a[i]) {
            ans += (prev - a[i]);
        }
        prev = a[i];
    }

    cout << ans << "\n";

    return 0;
}