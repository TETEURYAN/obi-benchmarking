
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (cin >> n) {
        long long sum = 0;
        int ans = -1;
        for (int i = 1; i <= n; ++i) {
            long long a;
            cin >> a;
            sum += a;
            if (sum >= 1000000 && ans == -1) {
                ans = i;
            }
        }
        cout << ans << "\n";
    }
    
    return 0;
}
