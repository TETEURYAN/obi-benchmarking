#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    long long sum = 0;
    int days = 0;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        sum += a;
        days++;
        if (sum >= 1000000) {
            break;
        }
    }

    cout << days << endl;
    return 0;
}