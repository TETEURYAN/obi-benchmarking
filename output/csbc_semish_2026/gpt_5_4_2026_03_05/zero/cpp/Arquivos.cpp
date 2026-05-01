#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long B;
    cin >> N >> B;

    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int i = 0, j = N - 1;
    int pastas = 0;

    while (i <= j) {
        if (i == j) {
            pastas++;
            break;
        }
        if (a[i] + a[j] <= B) {
            i++;
            j--;
        } else {
            j--;
        }
        pastas++;
    }

    cout << pastas << '\n';
    return 0;
}