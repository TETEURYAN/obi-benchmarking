
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ops = 0;
    while (true) {
        int min_val = a[0];
        int max_val = a[0];
        for (int i = 1; i < n; ++i) {
            if (a[i] < min_val) min_val = a[i];
            if (a[i] > max_val) max_val = a[i];
        }

        if (min_val == max_val) break;

        int start = -1;
        for (int i = 0; i < n; ++i) {
            if (a[i] == min_val) {
                start = i;
                break;
            }
        }

        for (int i = start; i < n && a[i] == min_val; ++i) {
            a[i]++;
        }
        ops++;
    }

    cout << ops << "\n";
    return 0;
}
