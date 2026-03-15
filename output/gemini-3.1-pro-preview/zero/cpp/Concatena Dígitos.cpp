
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        pref[i] = pref[i - 1] + x;
    }
    
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        long long k = r - l + 1;
        long long s = pref[r] - pref[l - 1];
        long long ans = 11LL * (k - 1) * s;
        cout << ans << "\n";
    }
    
    return 0;
}
