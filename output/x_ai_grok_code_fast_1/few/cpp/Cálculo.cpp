#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int M, N;
    cin >> M >> N;
    vector<int> X(M);
    for(int &x : X) cin >> x;
    vector<int> Y(N);
    for(int &y : Y) cin >> y;
    int L = max(M, N);
    while(X.size() < L) X.push_back(0);
    while(Y.size() < L) Y.push_back(0);
    vector<int> result(L + 1, 0);
    int carry = 0;
    for(int i = L - 1; i >= 0; i--) {
        int sum = X[i] + Y[i] + carry;
        result[i + 1] = sum % 2;
        carry = sum / 2;
    }
    // result[0] should be 0
    for(int i = 1; i <= L; i++) {
        if(i > 1) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}