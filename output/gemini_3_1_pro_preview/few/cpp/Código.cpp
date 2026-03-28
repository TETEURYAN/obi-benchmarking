#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (cin >> n) {
        vector<int> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }
        
        int ans = 0;
        for (int i = 0; i < n - 2; i++) {
            if (v[i] == 1 && v[i+1] == 0 && v[i+2] == 0) {
                ans++;
            }
        }
        
        cout << ans << "\n";
    }

    return 0;
}