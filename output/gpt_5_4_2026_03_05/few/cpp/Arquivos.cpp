#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    long long B;
    if (!(cin >> N >> B)) return 0;

    vector<long long> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    sort(a.begin(), a.end());

    int i = 0, j = N - 1;
    int ans = 0;

    while (i <= j) {
        if (i == j) {
            ans++;
            break;
        }
        if (a[i] + a[j] <= B) {
            i++;
            j--;
        } else {
            j--;
        }
        ans++;
    }

    cout << ans << '\n';
    return 0;
}