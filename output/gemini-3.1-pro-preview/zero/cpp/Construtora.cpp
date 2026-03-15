
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int ans = 0;
    while (true) {
        bool all_equal = true;
        for (int i = 1; i < n; i++) {
            if (a[i] != a[0]) {
                all_equal = false;
                break;
            }
        }
        if (all_equal) break;
        
        int min_val = a[0];
        for (int i = 1; i < n; i++) {
            if (a[i] < min_val) {
                min_val = a[i];
            }
        }
        
        int l = -1;
        for (int i = 0; i < n; i++) {
            if (a[i] == min_val) {
                l = i;
                break;
            }
        }
        
        int r = l;
        while (r + 1 < n && a[r + 1] == min_val) {
            r++;
        }
        
        for (int i = l; i <= r; i++) {
            a[i]++;
        }
        ans++;
    }
    
    cout << ans << "\n";
    
    return 0;
}
