
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (cin >> n) {
        vector<int> a(n + 1);
        int max_a = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            if (a[i] > max_a) {
                max_a = a[i];
            }
        }
        
        a[0] = max_a;
        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            if (a[i - 1] > a[i]) {
                ans += a[i - 1] - a[i];
            }
        }
        
        cout << ans << "\n";
    }
    return 0;
}
